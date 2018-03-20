#Code for motor driver and Infrared Sensors

 

import RPi.GPIO as GPIO

from time import sleep

 

GPIO.setwarnings(False)

 

Motor1A = 16

Motor1B = 18

Motor1E = 22

Motor3A = 19

Motor3B = 21

Motor3E = 23

 

def setup():

 

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(3,GPIO.IN)

    GPIO.setup(Motor1A,GPIO.OUT)

    GPIO.setup(Motor1B,GPIO.OUT)

    GPIO.setup(Motor1E,GPIO.OUT)

 

    GPIO.setup(5,GPIO.IN)

    GPIO.setup(Motor3A,GPIO.OUT)

    GPIO.setup(Motor3B,GPIO.OUT)

    GPIO.setup(Motor3E,GPIO.OUT)

 

def loop():

    while 1:

         if(GPIO.input(3)==GPIO.HIGH and GPIO.input(5)==GPIO.HIGH):

            print "Both wheels Forward"

            GPIO.output(Motor1A,GPIO.LOW)

            GPIO.output(Motor1B,GPIO.HIGH)

            GPIO.output(Motor1E,GPIO.HIGH)

            GPIO.output(Motor3A,GPIO.LOW)

            GPIO.output(Motor3B,GPIO.HIGH)

            GPIO.output(Motor3E,GPIO.HIGH)

 

         elif(GPIO.input(3)==GPIO.HIGH and GPIO.input(5)==GPIO.LOW):

             print "Turn left"

             GPIO.output(Motor1A,GPIO.LOW)

             GPIO.output(Motor1B,GPIO.HIGH)

             GPIO.output(Motor1E,GPIO.HIGH)

             GPIO.output(Motor3A,GPIO.HIGH)

             GPIO.output(Motor3B,GPIO.HIGH)

             GPIO.output(Motor3E,GPIO.LOW)

             #print"stop motor"

             #GPIO.output(Motor1E,GPIO.LOW)

             #GPIO.output(Motor3E,GPIO.LOW)

 

         elif(GPIO.input(3)==GPIO.LOW and GPIO.input(5)==GPIO.HIGH):

             print"Turn right"

             GPIO.output(Motor1A,GPIO.HIGH)

             GPIO.output(Motor1B,GPIO.HIGH)

             GPIO.output(Motor1E,GPIO.HIGH)

             GPIO.output(Motor3A,GPIO.LOW)

             GPIO.output(Motor3B,GPIO.HIGH)

             GPIO.output(Motor3E,GPIO.LOW)

 

         else:

             print"still"

             GPIO.output(Motor1B,GPIO.HIGH)

             GPIO.output(Motor1A,GPIO.HIGH)

             GPIO.output(Motor3B,GPIO.HIGH)

             GPIO.output(Motor3A,GPIO.HIGH)

             GPIO.output(Motor1E,GPIO.LOW)

             GPIO.output(Motor3E,GPIO.LOW)

             print "stop motor"

 

def destroy():

    GPIO.cleanup()

 

if __name__=='__main__':

    setup()

try:

    loop()

except KeyboardInterrupt:

     destroy()
