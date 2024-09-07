from atcoder.dsu import DSU

n,m=map(int,input().split())
d=DSU(n)
for _ in range(m):
    u,v=map(lambda x:x-1,map(int,input().split()))
    d.merge(u,v)
print(len(d.groups()))