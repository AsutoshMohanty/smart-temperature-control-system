# Smart Temperature Control System 🌡️

## About the Project
This is an IoT-based Smart Temperature Control System using Raspberry Pi Pico W and DHT22 sensor.

The system monitors temperature and humidity and automatically controls an LED as a fan indicator based on temperature.

## Components Used
- Raspberry Pi Pico W
- DHT22 Temperature and Humidity Sensor
- LED
- 220Ω Resistor
- Wokwi Simulator

## Features
- Real-time temperature monitoring
- Humidity monitoring
- Automatic temperature-based control
- LED ON when temperature reaches 30°C
- LED OFF when temperature falls below 28°C

## Working Principle
- Temperature ≥ 30°C: LED ON (Fan ON)
- Temperature below 28°C: LED OFF (Fan OFF)
- Between 28°C and 30°C: Previous state is maintained.

## Simulation
Built and tested using Wokwi.

## Project Files
- `main.py` – Python program
- `diagram.json` – Circuit connections

## Author
IoT Project – Smart Temperature Control System
