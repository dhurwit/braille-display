from sensorcontrol import Sensor
from steppercontrol import Motor
from solenoidcontrol import Solenoid

import time 
import sys
import RPi.GPIO as GPIO

SEN0 = 20
SEN1 = 19
SEN2 = 16

SOL0 = 13
SOL1 = 12
SOL2 = 6
SOL3 = 5
SOL4 = 25
SOL5 = 24

sensor = Sensor(SEN0, SEN1, SEN2)
solenoid = Solenoid(SOL0, SOL1, SOL2, SOL3, SOL4, SOL5)
motor = Motor()

def findfirstcolumn(pin):
    nextcolumn(pin) 
    
    timeout=time.time() + 1
    while sensor.edge_detect(pin) == 0 and time.time() > timeout:
        motor.onestep(REVERSE, MICROSTEP)
        time.sleep(0.01)
    if time.time() < timeout:
        findfirstcolumn()
    else:
        nextcolumn(pin)

def nextcolumn(pin):
    motor.onestep(forward, microstep)
    while sensor.edge_detect(pin) == 0:
        motor.onestep(forward, microstep)
        time.sleep(0.01)

def reset(pin, sol4, sol5, sol6):
    for i in range (0,39):
        solenoid.actuate(sol3)
        solenoid.actuate(sol4)
        solenoid.actuate(sol5)
        
        nextcolumn(pin)

def movecolumns(pin, num_columns):
    for i in range(1, num_columns):
        nextcolumn(pin)
