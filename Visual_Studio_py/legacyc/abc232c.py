from itertools import permutations

n,m=map(int,input().split())
connecta=[[False]*n for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1; b-=1
    connecta[a][b]=True
    connecta[b][a]=True

connectb=[[False]*n for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    a-=1; b-=1
    connectb[a][b]=True
    connectb[b][a]=True

for l in list(permutations(range(n),n)):
    f=True
    for i in range(n):
        for j in range(n):
            if connecta[i][j]!=connectb[l[i]][l[j]]:
                f=False
                break
        if not f: break
    if f:
        print('Yes')
        exit()
print('No')