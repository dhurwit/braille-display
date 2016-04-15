import RPi.GPIO as GPIO
import time

class Sensor:
    def __init__(self, s0_pin, s1_pin, s2_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(s0_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(s1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(s2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def edge_detect(self, pin):
        return GPIO.input(pin)

