from collections import defaultdict
from bisect import bisect_left, bisect_right

n,m=map(int,input().split())

A=[]
k=[]
for i in range(m):
    a=list(map(int,input().split()))
    A.append(a[1:])
    k.append(a[0])
b=list(map(int,input().split()))

d=defaultdict(int)
for i in range(n):
    d[b[i]]=i+1

maxday=[0]*m
for i in range(m):
    for j in range(k[i]):
        A[i][j]=d[A[i][j]]
        maxday[i]=max(maxday[i],A[i][j])

maxday.sort()
for i in range(1,1+n):
    print(bisect_right(maxday,i))