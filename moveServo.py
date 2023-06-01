import RPi.GPIO as GPIO
import pigpio

import math

GPIO.setmode(GPIO.BOARD)
pi=pigpio.pi()

x=0
y=1
z=2

tl1_pin, tl2_pin, tl3_pin = 2, 3, 4
tr1_pin, tr2_pin, tr3_pin = 17, 27, 22
br1_pin, br2_pin, br3_pin = 10, 9, 11
bl1_pin, bl2_pin, bl3_pin = 16, 20, 21

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

def moveServo(pin, ang):
    pi.set_servo_pulsewidth(pin,(ang*11.1111)+500)
    
def movingServo(tr_ang, br_ang, tl_ang, bl_ang):
    moveServo(tr1_pin,tr_ang[x]+10)
    moveServo(tr2_pin,180-(tr_ang[y]-23))
    moveServo(tr3_pin,tr_ang[z]-18)

    moveServo(tl1_pin,180-(tl_ang[x]+24))
    moveServo(tl2_pin,tl_ang[y]-10)
    moveServo(tl3_pin,180-(tl_ang[z])+18)
    
    moveServo(br1_pin,180-(br_ang[x]+13))
    moveServo(br2_pin,180-(br_ang[y]-17))
    moveServo(br3_pin,br_ang[z]-22)

    moveServo(bl1_pin,bl_ang[x]+10)
    moveServo(bl2_pin,bl_ang[y]-8)
    moveServo(bl3_pin,180-(bl_ang[z])+14)

