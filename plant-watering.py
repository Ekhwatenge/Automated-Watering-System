import time
import random

# Simulating sensor readings
def read_temperature():
    return round(random.uniform(20, 30), 2)

def read_humidity():
    return round(random.uniform(30, 70), 2)

def read_air_quality():
    return round(random.uniform(0, 100), 2)

# Main monitoring loop
def monitor_environment():
    while True:
        temperature = read_temperature()
        humidity = read_humidity()
        air_quality = read_air_quality()

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Air Quality Index: {air_quality}")
        print("--------------------")

        # Add logic for data storage or transmission here

        time.sleep(5)  # Wait for 5 seconds before next reading

if __name__ == "__main__":
    print("Environmental Monitoring System Started")
    monitor_environment()
