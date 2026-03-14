# \# Smart Public Washroom Hygiene Monitor

# 

# \## Overview

# The Smart Public Washroom Hygiene Monitor is an IoT-based system designed to monitor hygiene conditions in public washrooms such as those found in railway stations, malls, and universities. The system continuously tracks environmental parameters and alerts authorities when hygiene levels fall below acceptable standards.

# 

# The goal of this project is to improve sanitation management by providing real-time monitoring and data-driven maintenance decisions.

# 

# ---

# 

# \## Problem Statement

# Public washrooms often suffer from poor maintenance due to the lack of real-time monitoring systems. Issues such as bad odor, wet floors, empty soap dispensers, and high usage are usually identified only after complaints are made.

# 

# This project addresses that problem by using IoT sensors to automatically monitor washroom conditions and provide actionable data.

# 

# ---

# 

# \## Features

# \- Real-time monitoring of washroom hygiene parameters

# \- Detection of ammonia gas indicating bad odor

# \- Floor wetness detection

# \- Soap availability monitoring

# \- User count tracking

# \- Data logging and cloud integration

# \- Threshold-based alerts for maintenance staff

# 

# ---

# 

# \## Hardware Components

# \- Raspberry Pi

# \- Ammonia Gas Sensor

# \- IR Sensor

# \- Water Level / Moisture Sensor

# \- Soap Level Sensor

# \- Jumper Wires

# \- Breadboard

# \- Power Supply

# 

# ---

# 

# \## Software \& Technologies Used

# \- Python

# \- Raspberry Pi OS

# \- SSH (Secure Shell) for remote access

# \- Git \& GitHub for version control

# \- Google Sheets API (for cloud data logging)

# 

# ---

# 

# \## System Architecture

# 1\. Sensors collect environmental data from the washroom.

# 2\. Raspberry Pi processes the sensor data.

# 3\. Threshold conditions determine whether hygiene levels are acceptable.

# 4\. Data is sent to the cloud for monitoring and logging.

# 5\. Maintenance staff can review the data to take corrective action.

# 

# ---

# 

# \## Challenges Faced

# \- \*\*Hardware Limitation:\*\* Lack of a micro-HDMI to HDMI converter prevented direct monitor access, so SSH via Windows Terminal was used for remote configuration.

# \- \*\*Hardware Platform Migration:\*\* The system was initially planned using ESP32, but due to implementation challenges it was redesigned and implemented using Raspberry Pi within a limited time.

# \- \*\*Remote Access Issues:\*\* VNC Server configuration did not function as expected, so development was continued primarily through terminal access using SSH.

# 

# ---

# 

# \## Future Improvements

# \- Mobile application for real-time alerts

# \- Automated maintenance notifications

# \- Integration with municipal sanitation systems

# \- AI-based prediction of washroom maintenance needs

# 

# ---

# 

# \## Team

# IoT Capstone Project  

# Smart Hygiene Monitoring System

