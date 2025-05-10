from collections import deque

h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
t=s[:]

d=deque()
# 出口からBFS
for i in range(h):
    for j in range(w):
        if s[i][j]=='E':
            d.append((i,j))

vec=[(1,0,'^'),(-1,0,'v'),(0,1,'<'),(0,-1,'>')]
visited=[[False]*w for _ in range(h)]

while d:
    x,y=d.popleft()
    for dx,dy,dir in vec:
        nx,ny=x+dx,y+dy
        if 0<=nx<h and 0<=ny<w and s[nx][ny]=='.' and not visited[nx][ny]:
            d.append((nx,ny))
            visited[nx][ny]=True
            if s[nx][ny]=='.':
                t[nx][ny]=dir

for i in t:
    print(''.join(i))