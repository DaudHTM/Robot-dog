import RPi.GPIO as GPIO
import pigpio

import math
import Ik
import moveServo
import interpolate
GPIO.setmode(GPIO.BOARD)
pi=pigpio.pi()




#length of the thight and calves in cm
tigh, calve = 11.9824, 9.9847

z_offset=5.4

#IK variables

x=0
y=1
z=2

tr_ik=[0.0,0.0,0.0]
tl_ik=[0.0,0.0,0.0]
bl_ik=[0.0,0.0,0.0]
br_ik=[0.0,0.0,0.0]

tr_speed, br_speed, bl_speed, tl_speed= 1, 1, 1, 1

tr_Tang=[90.0,122.6,122.6]
tl_Tang=[90.0,122.6,122.6]
bl_Tang=[90.0,122.6,122.6]
br_Tang=[90.0,122.6,122.6]

tr_Cang=[90.0,122.6,122.6]
tl_Cang=[90.0,122.6,122.6]
bl_Cang=[90.0,122.6,122.6]
br_Cang=[90.0,122.6,122.6]



#pins for the motor driver
right_en, right_back, right_front = 8, 10, 12
left_en, left_back, left_front = 26, 24, 22

#output for the driver
GPIO.setup(left_front,GPIO.OUT)
GPIO.setup(left_back,GPIO.OUT)
GPIO.setup(left_en,GPIO.OUT)
GPIO.setup(right_back,GPIO.OUT)
GPIO.setup(right_front,GPIO.OUT)
GPIO.setup(right_en,GPIO.OUT)

GPIO.output(right_back, GPIO.LOW)
GPIO.output(right_front,GPIO.HIGH)

GPIO.output(left_back, GPIO.LOW)
GPIO.output(left_front,GPIO.HIGH)

right_motor=GPIO.PWM(right_en,1000)
left_motor=GPIO.PWM(left_en,1000)


right_motor.start(00)
left_motor.start(00)




try:
    while True:
        
        
        
        
        yas=10
        bas=0
        sped=0
        if int(tr_Cang[1])==int(tr_Tang[1]):
            Y=float(input("enter y dist "))
            X=float(input("enter x dist "))
            zat=float(input("etner z dist"))

        right_motor.start(0)
        left_motor.start(0)
        
        tr_Tang=Ik.IK(zat,X,Y)
        br_Tang=Ik.IK(zat,X,Y)
        bl_Tang=Ik.IK(-zat,X,Y)
        tl_Tang=Ik.IK(-zat,X,Y)
        
        while tr_Cang!=tr_Tang or tl_Cang!=tl_Tang:
            tr_Cang=interpolate.interpolate(1.5,tr_Tang[0],tr_Tang[1],tr_Tang[2],tr_Cang[0],tr_Cang[1],tr_Cang[2])
        
            tl_Cang=interpolate.interpolate(1.5,tl_Tang[0],tl_Tang[1],tl_Tang[2],tl_Cang[0],tl_Cang[1],tl_Cang[2])
            
            moveServo.movingServo(tr_Cang, br_Cang, tl_Cang, bl_Cang)
except KeyboardInterrupt:
    
    GPIO.cleanup()
