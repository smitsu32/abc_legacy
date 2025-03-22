from atcoder.dsu import DSU

n,m=map(int,input().split())
path=[0]*n
connect=[[]for _ in range(n)]
for i in range(m):
    ui,vi=map(int,input().split())
    ui-=1; vi-=1
    path[ui]+=1; path[vi]+=1
    connect[ui].append(vi)
    connect[vi].append(ui)
    
c=0     # 端点カウント
flag=True
for i in range(n):
    if path[i]==2:
        continue
    elif path[i]==1:
        c+=1
    else:
        flag=False  # 3点以上接続or独立点
        break
    
if c!=2:            # 円状or複数スティック状を省く
    flag=False
    
if not flag:
    print('No')
    exit()

d=DSU(n)

for i in range(n):
    for j in connect[i]:    # flagで省いたので約O(2n) 1--2--3--4--
        d.merge(i,j)

if d.size(0)==n:   # 連結か？
    print('Yes')
else:
    print('No')