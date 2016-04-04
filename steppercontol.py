import time
import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor


def turnoffmotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def microstep(numsteps):
    stepper.step(numsteps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)

mh = Adafruit_MotorHAT(addr= 0x60)
stepper = mh.getStepper(200, 1)
stepper.setSpeed(30)

atexit.register(turnoffmotors)


