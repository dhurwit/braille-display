#!/usr/bin/env python

import time
import os
import RPi.GPIO as GPIO
import csv
import sys

GPIO.setmode(GPIO.BCM)
DEBUG = 1
 
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)
 
        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low
 
        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1
 
        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
 
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
 
# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
 
# 10k trim pot connected to adc #0
fsr_adc = 0;
bit_log = []

def read_data(fsr_hertz, sol_hertz, filename, cycle_count):
    datalog = os.path.join(os.getcwd(), filename)
    sleep_time = (1.0 / fsr_hertz)
    end_count = int(((cycle_count / sol_hertz) * fsr_hertz))
    
    for i in range (0, end_count):
        fsr_bits = readadc(fsr_adc, SPICLK, SPIMOSI, SPIMISO, SPICS)   
        bit_log.append(fsr_bits)
        time.sleep(sleep_time)
        print fsr_bits

    GPIO.cleanup()
    with open(datalog, "w+") as output:
        print 'writing'
        writer = csv.writer(output, lineterminator = '\n')
        for val in bit_log:
            writer.writerow([val])
