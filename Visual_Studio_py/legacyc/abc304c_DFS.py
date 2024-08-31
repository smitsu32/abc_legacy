# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**6)

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
s=[0]

# DFS
while s:
    now=s.pop()     # 感染済の端点からまっすぐ探索
    for i in range(n):
        if i!=now:
            if virus[i]==False and dist(xy[now],xy[i]): # 未感染かつ距離内
                virus[i]=True
                s.append(i)

for i in virus:
    if i:
        print('Yes')
    else:
        print('No')