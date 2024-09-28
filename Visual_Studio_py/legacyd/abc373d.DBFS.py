from collections import deque
import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
INF=float('inf')

c=[[] for _ in range(n)]
for _ in range(m):
    u,v,w=map(int,input().split())
    u-=1; v-=1
    c[u].append([v,w])
    c[v].append([u,-w])

def bfs(i):
    d=deque()
    d.append(i)
    while d:
        u=d.popleft()
        for v,w in c[u]:
            if x[v]==-INF:
                d.append(v)
                x[v]=x[u]+w

# def dfs(u):
#     for v,w in c[u]:
#         if x[v]==-INF:
#             x[v]=x[u]+w
#             dfs(v)

x=[-INF]*n
for i in range(n):
    if x[i]==-INF:
        x[i]=0
        bfs(i)
        # dfs(i)
print(*x)