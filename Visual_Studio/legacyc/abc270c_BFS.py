from collections import deque
n,x,y=map(int,input().split())


connect=[[] for _ in range(n+1)]

# 点iと繋がっている点をconnect[i]に格納
for _ in range(n-1):
    u,v=map(int,input().split())
    connect[u].append(v)
    connect[v].append(u)
# print(connect)

# -1は未到達の点
# deque()はpopがはやい
used=[-1]*(n+1)
que=deque([x])

# BFS 点Xを始点として点iに繋がっている点をusedに格納
while len(que)>0:
    now=que.popleft()
    for to in connect[now]:
        if used[to]==-1:
            used[to]=now
            que.append(to)

# print(used)

# ゴールからたどりスタートでqueがゼロ
# 複数本伸びてるときでも最短でXに着ける
que=deque([y])
ans=[]
while len(que)>0:
    now=que.popleft()
    ans.append(now)
    
    to=used[now]
    if to!=x:       # xを見つけたら追加しない（ループ終了）
        que.append(to)

ans.append(x)   # 追加は別でする
print(*reversed(ans))