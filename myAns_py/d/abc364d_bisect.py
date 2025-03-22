from bisect import *

n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

# 範囲をb-mid~b+midに絞って個数を二分探索
for _ in range(q):
    b,x=map(int,input().split())
    ng,ok=-1,10**18  #個数
    while abs(ng-ok)>1:
        mid=(ok+ng)//2
        lb=bisect_left(a,b-mid)
        ub=bisect_right(a,b+mid)
        
        if ub-lb>=x:
            ok=mid
        else:
            ng=mid
    # print(ok,ng)
    print(ok)