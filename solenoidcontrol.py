import RPi.GPIO as GPIO
import time

class Solenoid:
    def __init__(self, s0_pin, s1_pin, s2_pin, s3_pin, s4_pin, s5_pin):
        GPIO.setup(s0_pin, GPIO.OUT)
        GPIO.setup(s1_pin, GPIO.OUT)
        GPIO.setup(s2_pin, GPIO.OUT)
        GPIO.setup(s3_pin, GPIO.OUT)
        GPIO.setup(s4_pin, GPIO.OUT)
        GPIO.setup(s5_pin, GPIO.OUT)

    def actuate(self, pin):
        GPIO.output(self.pin, True)
        time.sleep(0.05)
        GPIO.output(self.pin, False)
