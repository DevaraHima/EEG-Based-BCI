import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
motor1a=7
motor1b=11
motor2a=12
motor2b=13
motor3a=15
motor3b=16
motor4a=18
motor4b=22
GPIO.setup(motor1a,GPIO.OUT)
GPIO.setup(motor1b,GPIO.OUT)
GPIO.setup(motor2a,GPIO.OUT)
GPIO.setup(motor2b,GPIO.OUT)
GPIO.setup(motor3a,GPIO.OUT)
GPIO.setup(motor3b,GPIO.OUT)
GPIO.setup(motor4a,GPIO.OUT)
GPIO.setup(motor4b,GPIO.OUT)
x=[2, 1, 1, 0, 0, 0, 1, 3, 1, 3, 0, 2, 1, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 2, 3, 0, 2, 2, 2, 0, 1, 0, 1, 1, 0, 1,2, 1, 2, 2, 3, 2, 2, 3, 3, 3, 2, 2, 2, 1, 0, 0, 1, 2, 3, 1, 2, 0, 0, 0, 3, 1, 1, 0, 0, 2, 3, 2, 3, 3, 3, 0, 3,
2, 1, 3, 3, 1, 0, 1, 2, 2, 2, 3, 2, 0, 3, 1, 2, 1, 2, 3, 1, 3, 0, 0, 0, 3, 1, 0, 2, 0, 2, 1, 3, 0, 2, 2, 0, 2,1, 3, 3, 3, 2, 0, 2, 1, 3, 1, 0, 2, 1, 0, 2, 2, 0, 2, 3, 3, 1, 0, 1, 3, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 3, 0, 3,3, 3, 0, 0, 3, 1, 2, 3, 3, 0, 1, 2, 0, 3, 0, 3, 2, 1, 3, 2, 0, 1, 0, 2, 3, 1, 0, 0, 3, 1, 0, 2, 1, 1, 0, 0, 3,2, 0, 2, 2, 0, 1, 0, 1, 0, 0, 2, 2, 1, 2, 3, 0, 3, 0, 0, 1, 3, 2, 1, 3, 2, 3, 3, 3, 1, 1, 3, 0, 1, 0, 1, 2, 3,0, 3, 0, 2, 0, 3, 0, 2, 0, 1, 3, 2, 3, 0, 1, 3, 1, 2, 2, 0, 3, 1, 3, 1, 0, 2, 2, 1, 3, 1, 1, 0, 1, 3, 3, 1, 1,1, 1, 3, 3, 3, 3, 1, 1, 2, 1, 0, 3, 0, 3, 0, 0, 0, 0, 2, 2, 3, 1, 2, 2, 2, 3, 2, 0, 2]

n=len(x)
for i in range(n):
   if x[i]==0:
      GPIO.output(motor1a,GPIO.HIGH)
      GPIO.output(motor1b,GPIO.LOW)
      sleep(2)
      GPIO.output(motor1a,GPIO.LOW)
      GPIO.output(motor1b,GPIO.HIGH)
      sleep(2)
      GPIO.output(motor1b,GPIO.LOW)
      sleep(1)
   elif x[i]==1:
      GPIO.output(motor2a,GPIO.HIGH)
      GPIO.output(motor2b,GPIO.LOW)
      sleep(2)
      GPIO.output(motor2a,GPIO.LOW)
      GPIO.output(motor2b,GPIO.HIGH)
      sleep(2)
GPIO.output(motor2b,GPIO.LOW)
      sleep(1)
   elif x[i]==2:
      GPIO.output(motor3a,GPIO.HIGH)
      GPIO.output(motor3b,GPIO.LOW)
      sleep(2)
      GPIO.output(motor3a,GPIO.LOW)
      GPIO.output(motor3b,GPIO.HIGH)
      sleep(2)
      GPIO.output(motor3b,GPIO.LOW)
      sleep(1)
   elif x[i]==3:
      GPIO.output(motor4a,GPIO.HIGH)
      GPIO.output(motor4b,GPIO.LOW)
      sleep(2)
      GPIO.output(motor4a,GPIO.LOW)
      GPIO.output(motor4b,GPIO.HIGH)
      sleep(2)
      GPIO.output(motor4b,GPIO.LOW)
      sleep(1)
