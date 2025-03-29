from atcoder.dsu import DSU

n,m=map(int,input().split())

d=DSU(n)
dup=0 #閉路
for i in range(m):
    u,v=map(int,input().split())
    u-=1; v-=1
    if d.same(u,v):
        dup+=1
    d.merge(u,v)

print(dup)