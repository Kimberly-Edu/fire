import time
import RPi.GPIO as GPIO
import dht11  # Required module


def init():
    GPIO.setmode(GPIO.BCM)
    global dht11_inst
    dht11_inst = dht11.DHT11(pin=21)  # GPIO21


def read_temp():
    global dht11_inst
    result = dht11_inst.read()
    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        return result.temperature
    else:
        return 'X'  # Placeholder
