import random
import time
from datetime import datetime
import RPi.GPIO as GPIO
import paho.mqtt.publish as publish

# GPIO Setup
LED_PIN = 17
SOAP_LED_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SOAP_LED_PIN, GPIO.OUT)

# MQTT Broker Details
broker = "crystalmq.bevywise.com"
port = 1883
topic = "washroom/alert"

auth = {
    "username": "eCKpWBiq5LxgmbgqqR",
    "password": "vasusE7tKMYp3FEQ0f"
}

# System variables
people_count = 0
cleaning_required = False

# NEW SOAP VARIABLES
soap_level = 100
soap_threshold = 20
soap_refill_required = False

print("timestamp | humidity | gas% | people_count | soap_level | cleaning_required | LED")

while True:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Humidity simulation
    humidity = random.randint(40,70)

    # Simulate people entering (IR sensor)
    if random.random() < 0.35:
        people_count += 1

        # soap usage when people enter
        if soap_level > 0:
            soap_level -= random.randint(1,3)

    # Gas smell increases with people usage
    base_gas = 20 + (people_count * 5)
    gas_percent = base_gas + random.randint(-5,5)

    if gas_percent > 100:
        gas_percent = 100

    # Cleaning condition
    if humidity >= 65 and gas_percent >= 80 and people_count >= 10 and not cleaning_required:

        cleaning_required = True
        GPIO.output(LED_PIN, GPIO.HIGH)

        print("\n⚠ CLEANING REQUIRED ⚠")

        # Send MQTT Alert
        message = f"Washroom needs cleaning | Gas:{gas_percent}% | People:{people_count}"

        publish.single(
            topic=topic,
            payload=message,
            hostname=broker,
            port=port,
            auth=auth
        )

        print("MQTT Alert Sent")

    # SOAP REFILL CONDITION (NEW ADDITION)
    if soap_level <= soap_threshold and not soap_refill_required:

        soap_refill_required = True
        GPIO.output(SOAP_LED_PIN, GPIO.HIGH)

        print("\n🧼 SOAP REFILL REQUIRED")

        message = f"SOAP REFILL REQUIRED | Soap Level:{soap_level}%"

        publish.single(
            topic=topic,
            payload=message,
            hostname=broker,
            port=port,
            auth=auth
        )

        print("MQTT Soap Alert Sent")

    led_status = "ON" if cleaning_required else "OFF"

    print(f"{timestamp} | {humidity}% | {gas_percent}% | {people_count} | {soap_level}% | {'YES' if cleaning_required else 'NO'} | {led_status}")

    # Cleaning confirmation
    if cleaning_required:

        user_input = input("Has the washroom been cleaned? (yes/no): ")

        if user_input.lower() == "yes":

            print("Cleaning acknowledged. Resetting system...\n")

            cleaning_required = False
            people_count = 0

            GPIO.output(LED_PIN, GPIO.LOW)

    # SOAP REFILL CONFIRMATION (NEW ADDITION)
    if soap_refill_required:

        user_input = input("Has the dispenser been refilled? (yes/no): ")

        if user_input.lower() == "yes":

            print("Soap dispenser refilled. Resetting level...\n")

            soap_level = 100
            soap_refill_required = False

            GPIO.output(SOAP_LED_PIN, GPIO.LOW)

    time.sleep(3)