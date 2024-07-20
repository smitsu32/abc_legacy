# ABC276b UnionFind簡易版
n,m=map(int,input().split())
a=[]; b=[]
for _ in range(m):
    ai,bi=map(int,input().split())
    a.append(ai); b.append(bi)

ans=[[]for _ in range(n)]
# print(ans)
for i in range(m):
    c=a[i]-1; d=b[i]-1
    ans[c].append(b[i])
    ans[d].append(a[i])

# print(ans)
for i in range(n):
    b=ans[i]
    b.sort()
    print(len(b),*b)