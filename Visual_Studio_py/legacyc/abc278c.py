from collections import defaultdict

n,q=map(int,input().split())
f=defaultdict(set)  # O(1)で定義できる

for _ in range(q):
    t,a,b=map(int,input().split())
    a-=1; b-=1
    if t==1:
        f[a].add(b)
    elif t==2:
        f[a].discard(b)
    else:
        if b in f[a] and a in f[b]:
            print('Yes')
        else:
            print('No')