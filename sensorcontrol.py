import RPi.GPIO as GPIO
import time

class Sensor:
    def __init__(self, s0_pin, s1_pin, s2_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(s0_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(s1_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(s2_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.s0_pin = s0_pin
        self.s1_pin = s1_pin
        self.s2_pin = s2_pin

    def edge_detect0(self):
        return GPIO.input(self.s0_pin)
    
    def edge_detect1(self):
        return GPIO.input(self.s1_pin)
    
    def edge_detect2(self):
        return GPIO.input(self.s2_pin)

