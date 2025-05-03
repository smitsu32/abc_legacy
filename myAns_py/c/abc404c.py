from sys import setrecursionlimit
setrecursionlimit(10**7)

n,m=map(int,input().split())
connect=[[] for _ in range(n)]

for _ in range(m):
    a,b=map(int,input().split())
    a-=1; b-=1
    connect[a].append(b)
    connect[b].append(a)

if n!=m:
    print('No')
    exit()

for i in connect:
    if len(i)!=2:
        print('No')
        exit()


def dfs(v):
    visit[v]=True
    for i in connect[v]:
        if not visit[i]:
            dfs(i)

visit=[False]*n
dfs(0)
if visit.count(True)==n:
    print('Yes')
else:
    print('No')