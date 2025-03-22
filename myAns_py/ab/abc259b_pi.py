from math import atan2,pi,cos,sin

a,b,d=map(int,input().split())
r=(a**2+b**2)**0.5

theta=atan2(b,a)+d/180*pi   # atan2(y/x)=theta, tan(theta)=y/x

print(r*cos(theta),r*sin(theta))