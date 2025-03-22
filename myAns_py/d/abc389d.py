r=int(input())

ans=0
#毎xずつみていく(x=0.5,1.5,...)
#yは0.5ぶん下にずれているのでひく
for x in range(r):
    x+=0.5
    y=(r**2-x**2)**0.5-0.5
    ans+=int(y)
    if x==0.5: stock=ans

print(ans*4+1)