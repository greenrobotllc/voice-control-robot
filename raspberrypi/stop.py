# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
print " mode ="+str(mode)
GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepPinForward=18
StepPinBackward=16

StepPinForward2=13
StepPinBackward2=15


StepPinForward3=35
StepPinBackward3=37

StepPinForward4=38
StepPinBackward4=40
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)
GPIO.setup(StepPinForward2, GPIO.OUT)
GPIO.setup(StepPinBackward2, GPIO.OUT)
GPIO.setup(StepPinForward3, GPIO.OUT)
GPIO.setup(StepPinBackward3, GPIO.OUT)
GPIO.setup(StepPinForward4, GPIO.OUT)
GPIO.setup(StepPinBackward4, GPIO.OUT)
GPIO.output(StepPinForward, GPIO.LOW)
GPIO.output(StepPinForward2, GPIO.LOW)
GPIO.output(StepPinForward3, GPIO.LOW)
GPIO.output(StepPinForward4, GPIO.LOW)
    
GPIO.output(StepPinBackward, GPIO.LOW)
GPIO.output(StepPinBackward2, GPIO.LOW)
GPIO.output(StepPinBackward3, GPIO.LOW)
GPIO.output(StepPinBackward4, GPIO.LOW)
    
    
print "Stopping motor"
GPIO.cleanup()