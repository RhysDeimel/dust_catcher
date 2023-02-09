from machine import Pin, PWM
import time

pwm = PWM(Pin(16))  # GP16
pwm.freq(25000)  # 25kHz


# fan should stop @ 0% - but will go full power when no PWM detected
pwm.duty_u16(32768)  # duty 50% (65535/2)


def calc_duty(given_percentage):
    max_duty = 65535
    desired_duty = max_duty / (100 / given_percentage)

    return int(desired_duty)


# deque is not iterable in micropython - yet
# https://github.com/micropython/micropython-lib/pull/440
# need to use a dict that loops through numberical keys
from collections import deque

readings = deque((), 60)

PULSE = 2

rpm = 0


def callback(pin):
    global rpm
    rpm += 1


tacho = Pin(15, Pin.IN, Pin.PULL_UP)
tacho.irq(trigger=Pin.IRQ_RISING, handler=callback)

while True:
    readings.append(rpm)
    print(f"{rpm=} RPM")

    av_rpm = sum(readings) // len(readings)
    print(f"{rpm * 60 / 2} real")
    rpm = 0
    time.sleep(1)  # Detect every second


# TODO - detect rpm
# formula is:
# rpm = impulse frequency per second * 60 / 2
# fan has two impulses per revolution
# should wait 1 second between reads?
# pin needs a pull up resistor


# Gonna need to use interrupts?


# ripped from raspi code
# # Pin configuration
# TACH = 24       # Fan's tachometer output pin
# PULSE = 2       # Noctua fans puts out two pluses per revolution
# WAIT_TIME = 1   # [s] Time to wait between each refresh

# # Setup GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(TACH, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Pull up to 3.3V

# # Setup variables
# t = time.time()
# rpm = 0

# # Caculate pulse frequency and RPM
# def fell(n):
#     global t
#     global rpm

#     dt = time.time() - t
#     if dt < 0.005: return # Reject spuriously short pulses

#     freq = 1 / dt
#     rpm = (freq / PULSE) * 60
#     t = time.time()

# # Add event to detect
# GPIO.add_event_detect(TACH, GPIO.FALLING, fell)

# try:
#     while True:
#         print "%.f RPM" % rpm
#         rpm = 0
#         time.sleep(1)   # Detect every second

# except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
#     GPIO.cleanup() # resets all GPIO ports used by this function
