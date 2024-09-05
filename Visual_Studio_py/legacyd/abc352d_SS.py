from sortedcontainers import SortedList
from collections import defaultdict

n,k=map(int,input().split())
p=list(map(int,input().split()))

d=defaultdict(int)
for i,pi in enumerate(p):
    d[pi]=i

s=SortedList()  # 1個ずつ出し入れするのに便利
for i in range(1,k+1):
    s.add(d[i])

ans=s[-1]-s[0]      # index_max-index_min
for i in range(1,n-k+1):
    s.discard(d[i])
    s.add(d[i+k])       # 1個ずつ右移動
    
    ans=min(ans,s[-1]-s[0])

print(ans)