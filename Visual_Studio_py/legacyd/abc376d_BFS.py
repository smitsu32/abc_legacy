from collections import deque
INF=float('inf')

n,m=map(int,input().split())
c=[[] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1; b-=1
    c[a].append(b) #有効グラフ！！
    # c[b].append(a)

q=deque()
q.append(0) #頂点１だけでええやんけ！！！

d=[INF]*n
d[0]=0

while q:
    a=q.popleft()
    for i in c[a]:
        if d[i]==INF:
            d[i]=d[a]+1
        
        if i==0:
            print(d[a]+1)
            exit()
        
        q.append(i)
print(-1)