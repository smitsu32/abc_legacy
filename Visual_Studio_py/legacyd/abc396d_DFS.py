from collections import deque

n,m=map(int,input().split())
C=[[] for _ in range(n)]

for i in range(m):
    u,v,w=map(int,input().split())
    u-=1; v-=1
    C[u].append((v,w))
    C[v].append((u,w))

d=deque()
d.append((0,0)) # [i,cost]

visit=[False]*n

def dfs(i,cost):
    global ans
    visit[i]=True
    
    if i==n-1:
        ans=min(ans,cost)
    
    for v,w in C[i]:
        if not visit[v]:
            dfs(v,cost^w)
    
    visit[i]=False

ans=2**60+1
dfs(0,0)

print(ans)