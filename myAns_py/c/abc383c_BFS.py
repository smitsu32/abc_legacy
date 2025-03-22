from collections import deque

h,w,d=map(int,input().split())
s=[input() for _ in range(h)]

q=deque()
visit=set()
for i in range(h):
    for j in range(w):
        if s[i][j]=='H':
            q.appendleft((i,j,0))
            visit.add((i,j))

while q:
    i,j,dif=q.popleft()
    dif+=1
    if dif>d:
        continue
    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni,nj=i+di,j+dj
        if 0<=ni<h and 0<=nj<w and s[ni][nj]=='.' and (ni,nj) not in visit:
            visit.add((ni,nj))
            q.append((ni,nj,dif))

print(len(visit))