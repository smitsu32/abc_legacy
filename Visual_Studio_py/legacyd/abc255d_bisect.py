from bisect import *

n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
# print(a)
b=[0]
now=0
for i in range(n):
    now+=a[i]
    b.append(now)
# print(b)

# 二分探索してa[i]<=x<=a[i+1]をみつけ，別々に計算
for _ in range(q):
    x=int(input())
    ind=bisect_left(a,x)
    # print(ind,a[:ind],a[ind:])
    ans=x*ind-b[ind]
    ans+=(b[n]-b[ind])-x*(n-ind)
    print(ans)