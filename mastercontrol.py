from sensorcontrol import Sensor
from steppercontrol import Motor
from solenoidcontrol import Solenoid
from letterIdentification import Conversion 

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

def nextcolumn():
    motor.interleave(4, 30)
    while sensor.edge_detect0() == 0 and sensor.edge_detect1() == 0 and sensor.edge_detect2() == 0: 
        motor.interleave(1, 10)
        time.sleep(0.05)

def prevcolumn():
    motor.revinterleave(4, 30)
    while sensor.edge_detect0() == 0 and sensor.edge_detect1() == 0 and sensor.edge_detect2() == 0: 
        motor.revinterleave(1, 10)
        time.sleep(0.05)

def reset():
    for i in range (0,59):
        solenoid.actuate3()
        solenoid.actuate4()
        solenoid.actuate5()
        
        nextcolumn()

def movecolumns(num_columns):
    for i in range(1, num_columns):
        nextcolumn()

def moveback(number):
    for i in range(0, number):
        prevcolumn()

def movesteps(number):
    motor.singlestep(number,40)

def printtext(message):
    text = Conversion(message)
    text.toDots()
    sol0_list, sol1_list, sol2_list = text.toActuations()
    totalsteps = len(sol0_list)

    for i in range(0, totalsteps):     
        if sol0_list[i]:
            solenoid.actuate0()
        if sol1_list[i]:
            solenoid.actuate1()
        if sol2_list[i]:
            solenoid.actuate2()
        nextcolumn()

def control():
    message = raw_input('What would you like to say? (20 chars. max): ')
    if len(message) > 20:
        print 'Message too long, please re-enter.'
        control()
    movesteps(150)
    nextcolumn()
    reset()
    moveback(25)
    nextcolumn()
    printtext(message)
    movesteps(225)
    ask = raw_input('Would you like to print another message? (y/n): ')
    if ask == 'y':
        control()
    else:
        GPIO.cleanup()
        motor.turnoffmotors()
        sys.exit()


if __name__ == "__main__":
    control()    
