from collections import deque

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

virus=[False]*n     # 感染
virus[0]=True
q=deque()
q.append(0)

# BFS
while q:
    now=q.popleft()     # 感染済の端点を順に探索
    for i in range(n):
        if i!=now:
            if virus[i]==False and dist(xy[now],xy[i]): # 未感染かつ距離内
                virus[i]=True
                q.append(i)

for i in virus:
    if i:
        print('Yes')
    else:
        print('No')