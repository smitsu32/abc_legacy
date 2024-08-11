from collections import deque

def ne(i,j):        # '#'の隣接マスを返し、'#'の場合BFS
    next=[]
    st=[-1,0,1]
    for di in st:
        for dj in st:
            if not (di==0 and dj==0):
                if 0<=i+di<=h-1 and 0<=j+dj<=w-1:
                    next.append([i+di,j+dj])
    return next

def bfs(i,j):       # BFS(#をseenにし、mainで重複を防ぐ)
    que=deque()
    que.append((i,j))
    while que:
        fromi,fromj=que.popleft()
        for toi,toj in ne(fromi,fromj):
            if s[toi][toj]=='#' and not seen[toi][toj]:
                seen[toi][toj]=True
                que.append((toi,toj))


h,w=map(int,input().split())        # ここからmain
s=[list(input()) for _ in range(h)]

seen=[[False]*w for _ in range(h)]

ans=0
for i in range(h):                  # グループ左上の'#'をカウント
    for j in range(w):
        if s[i][j]=='#' and not seen[i][j]:
            bfs(i,j)
            seen[i][j]=True
            ans+=1
print(ans)