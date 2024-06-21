x,y,z=map(int,input().split())

if y<0:                     # 壁を+にすると楽
    x*=-1; y*=-1; z*=-1

if x<y:                 # 0x |  or  x0 |
    a=abs(x)
else:
    if y<z:             # 0|xz
        a=-1
    else:               # z0|x   or 0z|x
        a=abs(z)+(x-z)
print(a)