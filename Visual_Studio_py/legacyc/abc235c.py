from collections import defaultdict

n,q=map(int,input().split())
a=list(map(int,input().split()))

d=defaultdict(list)
for i in range(n):
    d[a[i]].append(i+1)
# print(d)

for _ in range(q):
    x,k=map(int,input().split())
    try:
        print(d[x][k-1])
    except:
        print(-1)