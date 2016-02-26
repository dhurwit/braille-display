import time
import RPi.GPIO as GPIO

def sol_loop (pin_num, reps, hertz):
    delay = (1.0 / hertz)
    GPIO.setmode(GPIO.BCM)
    solpin = pin_num
    GPIO.setup(solpin, GPIO.OUT)

    i = 0 
    try:
        for i in range (0, reps):
            GPIO.output(solpin, True)
            time.sleep(delay)
            GPIO.output(solpin, False)
            time.sleep(delay)
            i += 1
    except KeyboardInterrupt:
        GPIO.output(solpin, False)
        GPIO.cleanup()
        pass 
    
    GPIO.output(solpin, False)
