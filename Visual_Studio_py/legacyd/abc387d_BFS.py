from collections import deque

h,w=map(int,input().split())
s=[input() for _ in range(h)]
le,cr=[[1,0],[-1,0]],[[0,1],[0,-1]]

for i in range(h):
    for j in range(w):
        if s[i][j]=='G':
            E=(i,j)
        if s[i][j]=='S':
            S=(i,j)

ans=10**9

i,j=S
visit=set()
visit.add((i,j))
d=deque()
d.append((i,j,0))

# 縦から横
while d:
    i,j,now=d.popleft()
    if (i,j)==E:
        ans=min(ans,now)
        continue
    
    if now%2==0:
        for di,dj in le:
            ni,nj=i+di,j+dj
            if 0<=ni<h and 0<=nj<w and s[ni][nj]!='#' and (ni,nj) not in visit:
                d.append((ni,nj,now+1))
                visit.add((ni,nj))
    else:
        for di,dj in cr:
            ni,nj=i+di,j+dj
            if 0<=ni<h and 0<=nj<w and s[ni][nj]!='#' and (ni,nj) not in visit:
                d.append((ni,nj,now+1))
                visit.add((ni,nj))

# 横から縦
i,j=S
visit=set()
visit.add((i,j))
d.append((i,j,0))
while d:
    i,j,now=d.popleft()
    if (i,j)==E:
        ans=min(ans,now)
        continue
    
    if now%2==0:
        for di,dj in cr:
            ni,nj=i+di,j+dj
            if 0<=ni<h and 0<=nj<w and s[ni][nj]!='#' and (ni,nj) not in visit:
                d.append((ni,nj,now+1))
                visit.add((ni,nj))
    else:
        for di,dj in le:
            ni,nj=i+di,j+dj
            if 0<=ni<h and 0<=nj<w and s[ni][nj]!='#' and (ni,nj) not in visit:
                d.append((ni,nj,now+1))
                visit.add((ni,nj))

if ans!=10**9:
    print(ans)
else:
    print(-1)