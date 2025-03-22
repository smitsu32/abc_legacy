from collections import deque

n=int(input())
connect=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    connect[u].append(v)
    connect[v].append(u)

if len(connect[1])<=1:
    print(1)
    exit()

ans=[]
for ini in connect[1]:
    d=deque()
    d.append((ini))
    
    visit=set()
    visit.add(1)
    visit.add(ini)
    
    ansi=0
    while d:
        ansi+=1
        i=d.popleft()
        for next in connect[i]:
            if next not in visit:
                visit.add(next)
                d.append(next)
        
    ans.append(ansi)

ans.sort()
# print(ans)
print(sum(ans)-ans[-1] +1)  #点1のぶん