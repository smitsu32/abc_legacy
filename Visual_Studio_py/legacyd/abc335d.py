# 龍のしっぽ状にグリッド探索
n=int(input())

ans=[[0]*n for _ in range(n)]
ans[0][0]=1

# とぐろ状にx,yを返す
def next(x,y,now):
    vec=[(1,0),(0,1),(-1,0),(0,-1)]
    
    dx,dy=vec[now]
    if not (0<=x+dx<n and 0<=y+dy<n):
        now=(now+1)%4
        dx,dy=vec[now]
    elif ans[x+dx][y+dy]!=0:
        now=(now+1)%4
        dx,dy=vec[now]
    nex,ney=x+dx, y+dy
    
    return nex,ney,now

c=1
now=0
x,y=0,0
while True:
    c+=1
    x,y,now=next(x,y,now)
    ans[x][y]=c
    if x==n//2 and y==n//2:
        ans[x][y]='T'
        break

for i in ans:
    print(*i)