import rp2
import wifi
from machine import Pin, PWM
import fan
import web_server

# Set country code to allow use of correct WiFi channels
rp2.country("AU")

radio = wifi.WiFi("SausageSmugglers", "ChorizoSalami")
radio.connect()

fan_pin = PWM(Pin(16))  # GP16
fan_pin.freq(25000)  # 25kHz

fan_controller = fan.PWMFan(fan_pin)
