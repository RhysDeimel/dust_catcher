import network
import time


class WiFi:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wlan = network.WLAN(network.STA_IF)
        self.status = None

    def connect(self):
        self.wlan.active(True)
        self.wlan.connect(self.ssid, self.password)

        max_wait = 10
        while max_wait > 0:
            if self.wlan.status() < 0 or self.wlan.status() >= 3:
                break
            max_wait -= 1
            print("waiting for connection...")
            time.sleep(1)

        # Handle connection error
        if self.wlan.status() != 3:
            raise RuntimeError("network connection failed")
        else:
            print("WiFi connected")
            self.status = self.wlan.ifconfig()
            print(f"ip = {self.status[0]}")
