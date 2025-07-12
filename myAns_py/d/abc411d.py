from itertools import combinations

n,m=map(int, input().split())
g=[set() for _ in range(n)]
for _ in range(m):
    u,v=map(int, input().split())
    u-=1; v-=1
    if u>v: u,v=v,u
    g[u].add(v) #上三角行列

al=[] # すべての辺
for i in range(n-1):
    for j in range(i+1,n):
        al.append((i,j))

ans=10**18
for p in combinations(al,n): # 答えの辺の組み合わせを全試し
    ed=[0]*n # 辺の次数
    gnow=0 # 元からあった辺の数
    for u,v in p:
        ed[u]+=1
        ed[v]+=1
        if v in g[u]:
            gnow+=1
    
    if all(i==2 for i in ed): # すべての頂点のグラフの次数が2なら
        ansi=n+m-2*gnow # 追加＋削除辺 - 元の辺*2
        ans=min(ans,ansi)
print(ans)