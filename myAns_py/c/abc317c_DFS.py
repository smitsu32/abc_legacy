# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())

connect=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1; b-=1
    connect[a][b]=c
    connect[b][a]=c

ans=0
used=[False]*n

# DFS
def dfs(v,a):       # v:今の点 a:今の合計スコア
    global ans      # 値を維持
    used[v]=True
    ans=max(ans,a)      # ansは合計スコアの最大値
    for w in range(n):
        if connect[v][w] and not used[w]:       # 繋がってて未探索
            dfs(w,a+connect[v][w])              # 合計スコア+v->wのスコア
    used[v]=False                       # 何度でも同一点を探索できるため

for i in range(n):
    dfs(i,0)                # 始点任意,スタートスコア0

print(ans)