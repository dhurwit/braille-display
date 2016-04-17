import RPi.GPIO as GPIO
import time

class Solenoid:
    def __init__(self, s0_pin, s1_pin, s2_pin, s3_pin, s4_pin, s5_pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(s0_pin, GPIO.OUT)
        GPIO.setup(s1_pin, GPIO.OUT)
        GPIO.setup(s2_pin, GPIO.OUT)
        GPIO.setup(s3_pin, GPIO.OUT)
        GPIO.setup(s4_pin, GPIO.OUT)
        GPIO.setup(s5_pin, GPIO.OUT)
        self.s0_pin = s0_pin
        self.s1_pin = s1_pin
        self.s2_pin = s2_pin
        self.s3_pin = s3_pin
        self.s4_pin = s4_pin
        self.s5_pin = s5_pin


    def actuate0(self):
        GPIO.output(self.s0_pin, True)
        time.sleep(0.05)
        GPIO.output(self.s0_pin, False)
    
    def actuate1(self):
        GPIO.output(self.s1_pin, True)
        time.sleep(0.05)
        GPIO.output(self.s1_pin, False)

    def actuate2(self):
        GPIO.output(self.s2_pin, True)
        time.sleep(0.05)
        GPIO.output(self.s2_pin, False)
    
    def actuate3(self):
        GPIO.output(self.s3_pin, True)
        time.sleep(0.05)
        GPIO.output(self.s3_pin, False)

    def actuate4(self):
        GPIO.output(self.s4_pin, True)
        time.sleep(0.05)
        GPIO.output(self.s4_pin, False)
    
    def actuate5(self):
        GPIO.output(self.s5_pin, True)
        time.sleep(0.05)
        GPIO.output(self.s5_pin, False)
