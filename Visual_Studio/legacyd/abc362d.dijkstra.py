from heapq import heapify, heappop, heappush

n,m=map(int,input().split())
a=list(map(int,input().split()))

connect=[[] for _ in range(n)]
for _ in range(m):
    u,v,b=map(int,input().split())
    u-=1; v-=1
    connect[u].append([v,b+a[v]])       #u->v 辺の重みb, 到着した頂点の重みa[v]
    connect[v].append([u,b+a[u]])
# print(connect)

inf=10**18

start=0                 # 頂点１スタート
dist=[inf]*n        # １からの重み合計
dist[start]=0           # スタートの重みをゼロに

fin=[False]*n           # 距離が確定したら各点をTrueに

q=[(a[0],0)]              # スタートをキューに(heappopで重みを参照するため[重み, 点])
# heapify(q)                          # タプルを優先度付きキューに

while len(q)>0:
    d,now=heappop(q)                # heappop:重み(dist)の小さい順にとりだす
    if fin[now]:                    # もう確定してたらスキップ（ないとTLE）
        continue
    
    fin[now]=True                   # 最小値の点を確定
    
    for next, weight in connect[now]: # 繋がっているものを順に処理（BFSみたい）
        if not fin[next]:                           # 確定してないとき
            if dist[now]+weight<dist[next]:         # 距離が短かったら重みを更新
                dist[next]=dist[now]+weight
                heappush(q, (dist[next],next))      # nextをキューに追加

# print(dist)                                       # これで頂点1から各点の重みがdistに格納される

for i in range(n):
    dist[i]+=a[0]                                   # 頂点1の重みを足し忘れた

print(*dist[1:])
