from collections import deque

n=int(input())
xy=[]
grid=[[False]*3000 for _ in range(3000)]    #範囲設定が雑だとTLE
for _ in range(n):
    xi,yi=map(int,input().split())
    xi+=1000; yi+=1000
    xy.append([xi,yi])
    grid[yi][xi]=True

q=deque()
visit=[[False]*3000 for _ in range(3000)] #visitを管理しないと無限ループ
vec=((-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1))

# BFS
ans=0
for xi,yi in xy:
    if visit[yi][xi]==False: #まだxi,yi未探索なら
        q.append([xi,yi])
        visit[yi][xi]=True
        ans+=1
        
        while q:
            nx,ny=q.popleft()  

            for i,j in vec: #隣の黒マスがnot visitなら続けて処理
                if grid[ny+j][nx+i] and visit[ny+j][nx+i]==False:
                    visit[ny+j][nx+i]=True
                    q.append([nx+i,ny+j])
        
print(ans)