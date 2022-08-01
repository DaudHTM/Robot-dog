import RPi.GPIO as GPIO
import pigpio
from time import sleep
import math


GPIO.setmode(GPIO.BOARD)
pi=pigpio.pi()

# pins for all the servos
tl1_pin, tl2_pin, tl3_pin = 2, 3, 4
tr1_pin, tr2_pin, tr3_pin = 17, 27, 22
br1_pin, br2_pin, br3_pin = 10, 9, 11
bl1_pin, bl2_pin, bl3_pin = 16, 20, 21

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

tr_ang=[90.0,90.0,90.0]
tl_ang=[90.0,90.0,90.0]
bl_ang=[90.0,90.0,90.0]
br_ang=[90.0,90.0,90.0]



#servo pins as outputs
pi.set_mode(tr1_pin,pigpio.OUTPUT)
pi.set_mode(tr2_pin,pigpio.OUTPUT)
pi.set_mode(tr3_pin,pigpio.OUTPUT)
pi.set_mode(tl1_pin,pigpio.OUTPUT)
pi.set_mode(tl2_pin,pigpio.OUTPUT)
pi.set_mode(tl3_pin,pigpio.OUTPUT)
pi.set_mode(br1_pin,pigpio.OUTPUT)
pi.set_mode(br2_pin,pigpio.OUTPUT)
pi.set_mode(br3_pin,pigpio.OUTPUT)
pi.set_mode(bl1_pin,pigpio.OUTPUT)
pi.set_mode(bl2_pin,pigpio.OUTPUT)
pi.set_mode(bl3_pin,pigpio.OUTPUT)
pi.set_servo_pulsewidth(16,1800)

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

def moveServo(pin, ang):
    pi.set_servo_pulsewidth(pin,(ang*11.1111)+500)
    
def IK(x,y,z):
    
    if y<0:
        b=-1
    else:
        b=1
    y=abs(y)
    print(y)
    z=math.sqrt((y**2)+(z**2))
    yaa=math.atan(y/z)
    yaa=math.degrees(yaa)
    yaa=yaa*1.25
    xa=math.acos((((z**2)+(tigh**2))-(calve**2))/(2*z*tigh))
    xa=math.degrees(xa)
    ya=math.acos((((tigh**2)+(calve**2))-(z**2))/(2*tigh*calve))
    ya=math.degrees(ya)
    za=0
    print(yaa)
    tr_ang[1]=90-((xa*1.25)-12)+(yaa*1.25)
    tr_ang[2]=((ya-90)*1.25)+90



    
    return 0,xa,ya
    
    
def movingServo():
    moveServo(tr1_pin,tr_ang[x]+10)
    moveServo(tr2_pin,180-(tr_ang[y]+10))
    moveServo(tr3_pin,tr_ang[z]+13)

    moveServo(tl1_pin,180-(tl_ang[x]+24))
    moveServo(tl2_pin,tl_ang[y]+15)
    moveServo(tl3_pin,180-(tl_ang[z]+12))
    
    moveServo(br1_pin,180-(br_ang[x]+13))
    moveServo(br2_pin,180-(br_ang[y]+14))
    moveServo(br3_pin,br_ang[z]+4)

    moveServo(bl1_pin,bl_ang[x]+10)
    moveServo(bl2_pin,bl_ang[y]+17)
    moveServo(bl3_pin,180-(bl_ang[z]+19))




try:
    while True:
        
        
        movingServo()
        sleep(.2)
        yas=10
        bas=0
        sped=0
        yas=float(input("enter y dist "))
        bas=float(input("enter x dist "))
        sped=int(input("enter speed of motor"))
        if sped<0:
            GPIO.output(right_back, GPIO.HIGH)
            GPIO.output(right_front,GPIO.LOW)

            GPIO.output(left_back, GPIO.HIGH)
            GPIO.output(left_front,GPIO.LOW)
        else:
            GPIO.output(right_back, GPIO.LOW)
            GPIO.output(right_front,GPIO.HIGH)

            GPIO.output(left_back, GPIO.LOW)
            GPIO.output(left_front,GPIO.HIGH)
        sped=abs(sped)
        right_motor.start(sped)
        left_motor.start(sped)
        print(IK(0.0,bas,yas))
except KeyboardInterrupt:
    
    GPIO.cleanup()