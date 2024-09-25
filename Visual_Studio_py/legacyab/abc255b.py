n,k=map(int,input().split())
a=list(map(int,input().split()))
a=set(a)
x,y=[],[]
for _ in range(n):
    xi,yi=map(int,input().split())
    x.append(xi)
    y.append(yi)

xy=[]
for i in range(n):
    if i+1 in a:
        xyj=[]
        for j in range(n):
            xyj.append((abs(x[j]-x[i])**2+abs(y[j]-y[i])**2)**0.5)
        xy.append(xyj)

m=[0]*n
for i in range(n):
    mj=10**9
    for j in range(len(xy)):
        mj=min(mj,xy[j][i])
    m[i]=mj

print(max(m))