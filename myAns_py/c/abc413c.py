n,q=map(int,input().split())
a=list(map(int,input().split()))

b=[0]*(n+3) # 0:white, 1:black
ans=0
for ii in range(q):
    i=a[ii]
    if b[i]==0:
        if b[i-1]==1 and b[i+1]==1:
            ans-=1
        elif b[i-1]==1 or b[i+1]==1:
            ans=ans
        else:
            ans+=1
        b[i]=1
    else:
        if b[i-1]==1 and b[i+1]==1:
            ans+=1
        elif b[i-1]==1 or b[i+1]==1:
            ans=ans
        else:
            ans-=1
        b[i]=0
    print(ans)