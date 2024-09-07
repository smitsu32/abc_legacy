from atcoder.dsu import DSU

n,m=map(int,input().split())
d=DSU(n+1)

c=0
for _ in range(m):
    a,b=map(int,input().split())
    if d.same(a,b): # 閉路の数(既にa->o->bなら merge(a,b)で閉路になる)
        c+=1
    d.merge(a,b)

print(c)