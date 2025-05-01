# 01bfsによる実装 O(hw)

from collections import deque

h,w=map(int,input().split())
s=[input() for _ in range(h)]
a,b,c,d=map(int,input().split())
a-=1; b-=1; c-=1; d-=1

vec=[(1,0),(-1,0),(0,1),(0,-1)]

dist=[[10**18]*w for _ in range(h)] # 壁を壊す回数の最小値を格納
dist[a][b]=0 # スタート地点

q=deque()
q.append((0,a,b))
while q:
    kick,x,y=q.popleft()
    if dist[x][y]<kick:
        continue
    
    # 重み0
    for dx,dy in vec:
        nx,ny=x+dx,y+dy
        if 0<=nx<h and 0<=ny<w and s[nx][ny]==".":
            if dist[nx][ny]>kick: #壁を壊さずに移動し、回数が少なければ更新
                dist[nx][ny]=kick
                q.appendleft((kick,nx,ny))
    
    # 重み1
    for dx,dy in vec:
        for i in range(1,3): # 1~2マス先までの移動を考える
            nx,ny=x+dx*i,y+dy*i
            if 0<=nx<h and 0<=ny<w and dist[nx][ny]>kick+1: #壁を壊しても少なければ更新
                dist[nx][ny]=kick+1
                q.append((kick+1,nx,ny))

if dist[c][d]==10**18:
    print(-1)
else:
    print(dist[c][d])