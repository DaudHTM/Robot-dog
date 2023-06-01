

def interpolate(speed,tx,ty,tz,x,y,z):
    
    
    speedX=abs(tx-x)
    speedY=abs(ty-y)
    speedZ=abs(tz-z)
    
    ratioSpeed=max(speedX,speedY)
    ratioSpeed=max(ratioSpeed,speedZ)
    
    if ratioSpeed!=0:
        speedX=speedX/(ratioSpeed)
        speedY=speedY/(ratioSpeed)
        speedZ=speedZ/(ratioSpeed)
        speedX*=speed
        speedY*=speed
        speedZ*=speed
    elif ratioSpeed==0:
        speedX=0
        speedY=0
        speedZ=0
    

    
    if x<tx:
        x=x+speedX
    elif x>tx:
        x=x-speedX
    
    if y<ty:
        y=y+speedY
    elif y>ty:
        y=y-speedY
    
    if z<tz:
        z=z+speedZ
    elif z>tz:
        z=z-speedZ
 
    
    if tx-x>-2 and tx-x<2:
        x=tx
    if ty-y>-2 and ty-y<2:
        y=ty
    if tz-z>-2 and tz-z<2:
        z=tz
    return x,y,z
    
    
    