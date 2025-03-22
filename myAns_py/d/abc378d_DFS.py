import sys
sys.setrecursionlimit(10**7)

h,w,K=map(int,input().split())
s=[input() for _ in range(h)]
vec=[[1,0],[-1,0],[0,1],[0,-1]]

def dfs(i,j,k): #DFS中に回数もおけばよい
    global ans
    if k==K:
        ans+=1
        return
    
    visit[i][j]=True
    for di,dj in vec:
        if 0<=i+di<h and 0<=j+dj<w and not visit[i+di][j+dj] and s[i+di][j+dj]=='.':
            dfs(i+di,j+dj,k+1)
    
    visit[i][j]=False #別の点から始めたときに通れるように
    

ans=0
visit=[[False]*w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            continue
        
        dfs(i,j,0)

print(ans)