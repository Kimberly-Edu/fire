import RPi.GPIO as GPIO


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.IN)  # GPIO17


def read_ir():
    if GPIO.input(17) == 0:  # 0 == white/air, 1 == black/fire
        print("Fire Detected!")
        return True
    else:
        return False
