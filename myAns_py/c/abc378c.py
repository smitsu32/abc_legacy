from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))
d=defaultdict(int)

ans=[]
for i in range(n):
    if d[a[i]]==0:
        ans.append(-1)
    else:
        ans.append(d[a[i]])
    
    d[a[i]]=i+1

print(*ans)