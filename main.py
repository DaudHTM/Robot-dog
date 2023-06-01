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
stated = 0
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
        walkXspeed=.4
        walkYspeed=.4
        """
        if int(tr_Cang[1])==int(tr_Tang[1]):
            Y=float(input("enter y dist "))
            X=float(input("enter x dist "))
            zat=float(input("etner z dist"))
        """
        right_motor.start(0)
        left_motor.start(0)
      
        
        if stated==0:
            tl_Tang=Ik.IK(0,-3,18)
            tr_Tang=Ik.IK(0,-3,13)
            bl_Tang=Ik.IK(0,-3,13)
            br_Tang=Ik.IK(0,-3,18)
            walkYspeed=.65
            walkXspeed=.65
        elif stated==1:
            tl_Tang=Ik.IK(0,-3,13)
            tr_Tang=Ik.IK(0,-3,18)
            bl_Tang=Ik.IK(0,-3,18)
            br_Tang=Ik.IK(0,-3,13)
            walkYspeed=.65
            walkXspeed=.65
        elif stated==2:
            tl_Tang=Ik.IK(0,-3,18)
            tr_Tang=Ik.IK(0,-3,13)
            bl_Tang=Ik.IK(0,-3,13)
            br_Tang=Ik.IK(0,-3,18)
            walkXspeed=.65
            walkYspeed=.65
        elif stated==3:
            tl_Tang=Ik.IK(0,-3,13)
            tr_Tang=Ik.IK(0,-3,18)
            bl_Tang=Ik.IK(0,-3,18)
            br_Tang=Ik.IK(0,-3,13)
            walkXspeed=.65
            walkYspeed=.65
            
        while tr_Cang!=tr_Tang or tl_Cang!=tl_Tang:
            tr_Cang=interpolate.interpolate(walkYspeed,tr_Tang[0],tr_Tang[1],tr_Tang[2],tr_Cang[0],tr_Cang[1],tr_Cang[2])
        
            br_Cang=interpolate.interpolate(walkXspeed,br_Tang[0],br_Tang[1],br_Tang[2],br_Cang[0],br_Cang[1],br_Cang[2])
            
            tl_Cang = br_Cang
            bl_Cang = tr_Cang
            moveServo.movingServo(tr_Cang, br_Cang, tl_Cang, bl_Cang)
        stated +=1
        if stated>3:
            stated=0
except KeyboardInterrupt:
    
    GPIO.cleanup()
