# ABC350D亜種
from collections import deque

n,m=map(int,input().split())
connect=[[] for _ in range(n)]
for _ in range(m):
    u,v,w=map(int,input().split())
    connect[u-1].append((v-1,w)) # 有向！！！！

v1=[False]*n
v1[0]=True
def dfs(i):
    if i==n-1:
        return True
    
    for j,w in connect[i]:
        if not v1[j]:
            v1[j]=True
            if dfs(j):
                return True
    return False

if not dfs(0):
    print(-1)
    exit()

ans=1<<60
visited=set()

q=deque()
q.append((0,0)) # ノード、XOR

while q:
    i,now=q.popleft()
    
    if (i,now) in visited:
        continue
    
    visited.add((i,now))
    
    if i==n-1:
        ans=min(ans,now)
    
    for j,w in connect[i]:
        new_xor=now^w
        if (j,new_xor) not in visited:
            q.append((j,new_xor))

print(ans)