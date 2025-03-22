from collections import defaultdict

n=int(input())
connect=defaultdict(list)       # 点の数が10**9のため
for _ in range(n):
    ai,bi=map(int,input().split())
    connect[ai].append(bi)
    connect[bi].append(ai)

q=list()
q.append(1)
visited=set()                   # 同上
visited.add(1)

# DFS
while q:
    now=q.pop() 
    for i in connect[now]:
        if not i in visited:
            q.append(i)
            visited.add(i)

print(max(visited))