
import math


tigh, calve = 11.9824, 9.9847

z_offset=5.4

def IK(x,y,z):
    asd=1
    x=x+5.4
    if x<0:
        asd=-1
    b=1
    if y<0:
        b=-1
    x=abs(x)
    zAng1=math.atan(x/z)
    zAng1=math.degrees(zAng1)
    zHyp=math.sqrt((x**2)+(z**2))
    newZ=math.sqrt((zHyp**2)-(z_offset**2))
    
    zAng2=math.atan(newZ/z_offset)
    zAng2=math.degrees(zAng2)
    zAng=zAng1+zAng2
    z=newZ
    
    
    
    y=abs(y)
    yAng=math.atan(y/z)
    yAng=math.degrees(yAng)
    yHyp=math.sqrt((y**2)+(z**2))
    
    z=yHyp
    
    xa=math.acos((((z**2)+(tigh**2))-(calve**2))/(2*z*tigh))
    xa=math.degrees(xa)
    ya=math.acos((((tigh**2)+(calve**2))-(z**2))/(2*tigh*calve))
    ya=math.degrees(ya)
  
 
    
    zAng=90-((90-zAng)*1.75)
    yAng=122.6-((xa*1.363)-(yAng*1.363*b))
    xAng=ya*1.363
    
    return(zAng,yAng,xAng)
