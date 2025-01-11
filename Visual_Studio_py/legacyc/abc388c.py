from bisect import *

n=int(input())
a=list(map(int,input().split()))
a.sort()

ans=0
for i in range(n):
    ans+=bisect_right(a,a[i]//2)

print(ans)