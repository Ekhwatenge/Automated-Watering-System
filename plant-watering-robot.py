import RPi.GPIO as GPIO
import time
from gpiozero import MCP3008

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define pins
MOISTURE_SENSOR_PIN = 0  # Connected to MCP3008 channel 0
PUMP_PIN = 17

# Set up pump pin as output
GPIO.setup(PUMP_PIN, GPIO.OUT)

# Create ADC object for moisture sensor
adc = MCP3008(channel=MOISTURE_SENSOR_PIN)

# Define moisture thresholds
DRY_THRESHOLD = 0.7
WET_THRESHOLD = 0.3

def read_moisture():
    return adc.value

def water_plant(duration):
    GPIO.output(PUMP_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(PUMP_PIN, GPIO.LOW)

try:
    while True:
        moisture = read_moisture()
        print(f"Moisture level: {moisture:.2f}")

        if moisture > DRY_THRESHOLD:
            print("Soil is dry. Watering plant...")
            water_plant(5)  # Water for 5 seconds
        elif moisture < WET_THRESHOLD:
            print("Soil is sufficiently moist.")
        else:
            print("Soil moisture is optimal.")

        time.sleep(300)  # Wait for 5 minutes before next check

except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    GPIO.cleanup()
