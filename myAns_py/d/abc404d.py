import sys
from itertools import product
input = sys.stdin.readline

n,m=map(int,input().split())
c=list(map(int,input().split()))

zoo=[[] for _ in range(n)]
for i in range(m):
    a=list(map(int,input().split()))
    for j in a[1:]:
        zoo[j-1].append(i)

ans=float('inf')

for use in product(range(3), repeat=n):
    animal=[0]*m
    cost=0
    for i in range(n):
        for j in zoo[i]:
            animal[j]+=use[i]
        cost+=use[i]*c[i]
    
    if all(count>=2 for count in animal):
        ans=min(ans,cost)

print(ans)