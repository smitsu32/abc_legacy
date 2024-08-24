# 木、グラフ問題
n,k=map(int,input().split())

connect=[set() for _ in range(n)]       # set
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    connect[a].add(b)
    connect[b].add(a)
# print(connect)

v=list(map(int,input().split()))  # in の探索を早くするためset
for i in range(k):
    v[i]-=1
v=set(v)

# 木問題(Vに含まれない葉(末端の点)を消せるか判定)
q=[]
for i in range(n):
    if len(connect[i])==1:
        q.append(i)

ans=n                           # 点の数
for i in q:
    if i not in v:              # 消してもいいなら(vにないなら)
        ans-=1

        vno=connect[i].pop()        # 枝を削除 (pop:取出, discard:removeの上位互換)
        connect[vno].discard(i)
        if len(connect[vno])==1:           # 独立葉が新たに生じたらqに追加
            q.append(vno)

print(ans)