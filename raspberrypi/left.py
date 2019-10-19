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

def left(x):
    fast= 100 #input("How fast? (20-100)")
    slow= 30 #input("How fast? (20-100)")
    my_pwm=GPIO.PWM(StepPinForward,100)
    my_pwm.start(0)
    my_pwm.ChangeDutyCycle(slow)
    
    my_pwm2=GPIO.PWM(StepPinForward2,100)
    my_pwm2.start(0)
    my_pwm2.ChangeDutyCycle(fast)
    
    my_pwm3=GPIO.PWM(StepPinForward3,100)
    my_pwm3.start(0)
    my_pwm3.ChangeDutyCycle(slow)
    
    my_pwm4=GPIO.PWM(StepPinForward4,100)
    my_pwm4.start(0)
    my_pwm4.ChangeDutyCycle(fast)
    
    
    time.sleep(x)
    my_pwm.stop()
    GPIO.cleanup()

left(3)
