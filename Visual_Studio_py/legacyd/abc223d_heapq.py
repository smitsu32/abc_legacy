from heapq import heapify,heappop,heappush

n,m=map(int,input().split())

out=[0]*n   #有向グラフの終点管理
connect=[[] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1; b-=1
    out[b]+=1
    connect[a].append(b)

q=[]    #プライオリティキューで先頭を管理
for i in range(n):
    if out[i]==0:
        q.append(i)
        
heapify(q)

ans=[]
while q:
    now=heappop(q)
    ans.append(now+1)
    
    #BFS
    for to in connect[now]:
        out[to]-=1
        if out[to]==0:
            heappush(q,to)

if len(ans)<n:
    print(-1)
else:
    print(*ans)