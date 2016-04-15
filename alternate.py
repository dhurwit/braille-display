import RPi.GPIO as GPIO
import time
import sys

def sol_loop (pin1, pin2, reps, hertz):
    delay = (1.0 / hertz)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)

    for i in range (0, reps, 2):
        GPIO.output(pin1, True)
        time.sleep(delay)
        GPIO.output(pin1, False)
        time.sleep(delay)
            
        GPIO.output(pin2, True)
        time.sleep(delay)
        GPIO.output(pin2, False)
        time.sleep(delay) 
   
    GPIO.output(pin1, False)
    GPIO.output(pin2, False)
    GPIO.cleanup()
