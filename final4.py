import RPi.GPIO as GPIO
import time
import random
from datetime import datetime

GPIO.setmode(GPIO.BCM)

GAS_PIN = 17
LED_PIN = 27

GPIO.setup(GAS_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

people_count = 0

print("timestamp | humidity | gas% | people_count | cleaning_required | LED")

try:
    while True:

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Simulated humidity
        humidity = random.randint(40,75)

        # Gas sensor
        gas_state = GPIO.input(GAS_PIN)

        if gas_state == 1:
            gas_percent = random.randint(60,100)
        else:
            gas_percent = random.randint(5,30)

        # Simulated IR counter
        people_count += random.randint(0,1)

        # Cleaning condition
        if gas_percent >= 80:
            GPIO.output(LED_PIN, GPIO.HIGH)
            cleaning_status = "YES"
            led_status = "ON"
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            cleaning_status = "NO"
            led_status = "OFF"

        # Column format output
        print(f"{timestamp} | {humidity}% | {gas_percent}% | {people_count} | {cleaning_status} | {led_status}")

        time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()
