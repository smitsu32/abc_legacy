from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))

d=defaultdict(int)
pos=defaultdict(list)
for i in range(n):
    d[a[i]]+=1
    pos[a[i]].append(i+1)

ans,ansi=-1,-1
for i in d:
    if d[i]==1 and i>ansi:
        ans=pos[i][0]
        ansi=i
print(ans)