from collections import deque,defaultdict

n=int(input())
connect=defaultdict(list)       # 点の数が10**9のため
for _ in range(n):
    ai,bi=map(int,input().split())
    connect[ai].append(bi)
    connect[bi].append(ai)

q=deque()
q.append(1)
visited=set()                   # 同上
visited.add(1)

# BFS
while q:
    now=q.popleft() 
    for i in connect[now]:
        if not i in visited:
            q.append(i)
            visited.add(i)

print(max(visited))