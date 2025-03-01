from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))

d=defaultdict(list)
for i in range(n):
    d[a[i]].append(i)

ans=10**9
for di in d:
    l=len(d[di])
    if l>=2:
        for i in range(l-1):
            ans=min(ans,d[di][i+1]-d[di][i]+1)

if ans==10**9:
    print(-1)
else:
    print(ans)