import rp2
import wifi
import web_server
import fan

# Set country code to allow use of correct WiFi channels
rp2.country("AU")

radio = wifi.WiFi("SausageSmugglers", "ChorizoSalami")
radio.connect()

fan.PWMFan().speed = 50

web_server.app.start()
