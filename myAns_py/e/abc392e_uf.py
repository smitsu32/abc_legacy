from atcoder.dsu import DSU

n,m=map(int,input().split())
d=DSU(n)
res=[]
for i in range(m):
    a,b=map(int,input().split())
    a-=1; b-=1
    if d.same(a,b):
        res.append((a,i)) #重複の辺番号iと点a
    d.merge(a,b)

lead={d.leader(i) for i in range(n)} #set

# 繋がっていない点を重複辺で繋げる
ans=[]
for a,i in res:
    for b in lead:
        if not d.same(a,b):
            ans.append((i+1,a+1,b+1))
            d.merge(a,b)
            lead.discard(b)
            break

print(len(ans))
for i in ans:
    print(*i)