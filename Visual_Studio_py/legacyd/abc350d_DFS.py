# CPythonで実行すること！！！！！！！！

import sys
sys.setrecursionlimit(10**6)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

n,m=map(int,input().split())
connect=[[] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    a-=1; b-=1
    connect[a].append(b)
    connect[b].append(a)

def dfs(i):
    cnt=1 #辺の数
    visit[i]=True
    for j in connect[i]:
        if not visit[j]:
            cnt+=dfs(j)
    
    return cnt

ans=0
visit=[False]*n
for i in range(n):
    if not visit[i]:
        ansi=dfs(i)
        ans+=ansi*(ansi-1)//2 #1~cnt-1 (その点は含まず)

print(ans-m)