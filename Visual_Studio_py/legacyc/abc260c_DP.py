n,x,y=map(int,input().split())

r,b=[0]*n,[0]*n
r[0]=1

for i in range(n-1):
    b[i]+=r[i]*x
    r[i+1]=r[i]+b[i]
    b[i+1]=b[i]*y
