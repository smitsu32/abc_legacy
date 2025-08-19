n,m=map(int,input().split())
x=list(map(int,input().split()))
x.sort()

g=[]
for i in range(n-1):
    g.append(x[i+1]-x[i]) # 差

if n==m:
    print(0)
    exit()

l,r=-1,10**12+1
while abs(l-r)>1:
    mid=(l+r)//2
    count=0
    for i in g:
        if i<=mid:
            count+=1
    
    if count>=n-m: # n-m 個に分けられるなら
        r=mid
    else:
        l=mid

ans=0
for i in range(len(g)):
    if g[i]<r:
        ans+=g[i]
ansm=0
for i in range(len(g)):
    if g[i]<r:
        ansm+=1

ans+=(n-m-ansm)*r

print(ans)