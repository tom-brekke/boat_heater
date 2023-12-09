#!/usr/bin/env python
from __future__ import print_function
import subprocess 
import time
import sys

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)


def fileexists(filename):
    try:
        with open(filename): pass
    except IOError:
            return False
    return True

def GetTemperature():
    subprocess.call(['/sbin/modprobe', 'w1-gpio'])
    subprocess.call(['/sbin/modprobe', 'w1-therm'])

    filename = '/sys/bus/w1/devices/28-3c01b55653d2/w1_slave'
    if fileexists(filename):
        tfile = open(filename)
    else:
        return "no file"

    text = tfile.read()
    tfile.close()

    secondline = text.split("\n")[1]
    tempdata = float(secondline.split("=")[1])
    tempdata = tempdata / 1000

    return(tempdata)




def main(low, high, upper):
    for i in range(0,upper):
        temp = float(GetTemperature())
        print("Temperature is currently:", temp, file=sys.stdout)
        sys.stdout.flush()
        if temp < low:
            GPIO.output(2,GPIO.HIGH)
        if temp > high:
            GPIO.output(2,GPIO.LOW)
        time.sleep(1)
    print("done", file=sys.stderr)    

if __name__ == "__main__":
    low =    float(raw_input("What is the lower bound?  "    ))
    high =   float(raw_input("What is the upper bound?  "    ))
    upperH = float(raw_input("For many hours should I run?  "))
    upperM = upperH *60
    upperS = upperM *60
    upper = int(max(1.0, upperS))
    
main()
GPIO.cleanup()
