from atcoder.dsu import DSU

n,d=map(int,input().split())
xy=[]
for i in range(n):
    x,y=map(int,input().split())
    xy.append([x,y])
    
def dist(a,b):
    if (a[0]-b[0])**2+(a[1]-b[1])**2<=d**2:
        return True
    else:
        return False

x0,y0=xy[0]
dsu=DSU(n)
for i in range(n):
    for j in range(i,n):
        if i==j: continue
        
        if dist(xy[i],xy[j]):
            dsu.merge(j,i)

for i in range(n):
    if dsu.leader(i)==dsu.leader(0):        # リーダー点が０なら(==0はダメ)
        print('Yes')
    else:
        print('No')