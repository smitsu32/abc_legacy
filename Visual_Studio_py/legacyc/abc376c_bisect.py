n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()

ok,ng=10**18,0
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    c=sorted(b+[mid])
    
    for i in range(n):
        if a[i]>c[i]:
            ng=mid
            break
    else:
        ok=mid

if ok!=10**18:
    print(ok)
else:
    print(-1)