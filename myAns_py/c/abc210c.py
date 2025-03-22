from collections import defaultdict

n,k=map(int,input().split())
c=list(map(int,input().split()))

d=defaultdict(int)
s=set()

for i in range(k):
    s.add(c[i])
    d[c[i]]+=1

ans=len(s)
for i in range(n-k):
    d[c[i]]-=1
    d[c[i+k]]+=1
    s.add(c[i+k])
    if d[c[i]]==0:
        s.discard(c[i])
    ans=max(ans,len(s))
    
print(ans)