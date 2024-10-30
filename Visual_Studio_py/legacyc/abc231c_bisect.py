n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

for i in range(q):
    x=int(input())
    ok,ng=n,-1
    while abs(ok-ng)>1:
        mid=(ok+ng)//2
        if a[mid]>=x:
            ok=mid
        else:
            ng=mid
    print(n-ok) #okはxより小さい数