# AHT20 Temperature and Humidity Sensor
# https://github.com/adafruit/Adafruit_CircuitPython_AHTx0


import time
import board
import adafruit_ahtx0

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

# while True:
#     print("\nTemperature: %0.1f C" % sensor.temperature)
#     print("Humidity: %0.1f %%" % sensor.relative_humidity)
#     time.sleep(2)
