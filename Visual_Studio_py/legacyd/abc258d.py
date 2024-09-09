n,x=map(int,input().split())
a,b=[],[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)

c=[]
now=0
for i in range(n):
    now+=a[i]+b[i]
    c.append(now)
    
ans=10**100
for i in range(x):
    if i<n:
        ans=min(ans,c[i]+b[i]*(x-i-1))  # i回まで通常クリア、その後x回までb[i]を連打
    else:
        break
print(ans)