n=int(input())
X,Y=[0]*n,[0]*n
for i in range(n):
    X[i],Y[i]=map(int,input().split())
s=input()

yl,yr=dict(),dict()
for i in range(n):
    x,y=X[i],Y[i]
    if s[i]=='R':
        if y not in yl:
            yl[y]=x
        else:
            yl[y]=min(yl[y],x)
    else:
        if y not in yr:
            yr[y]=x
        else:
            yr[y]=max(yr[y],x)

for y in yl:
    if y in yr and yl[y]<yr[y]:
        print('Yes')
        exit(0)
print('No')