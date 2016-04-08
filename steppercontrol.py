import atexit
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

class Motor:
    def __init__(self):
        self.mh = Adafruit_MotorHAT(addr= 0x60)
        self.stepper = self.mh.getStepper(200, 1)
        

    def turnoffmotors(self):
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


    def microstep(self, numsteps, speed):
        self.stepper.setSpeed(speed)
        self.stepper.step(numsteps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.MICROSTEP)


    def revmicrostep(self, numsteps, speed):
        self.stepper.setSpeed(speed)
        self.stepper.step(numsteps, Adafruit_MotorHAT.REVERSE, Adafruit_MotorHAT.MICROSTEP)


    def singlestep(self, numsteps, speed):
        self.stepper.setSpeed(speed)
        self.stepper.step(numsteps, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)


    def onestep(self, direction, style):
        self.stepper.oneStep(direction, style)
       




