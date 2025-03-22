from itertools import permutations

n,mg=int(input()),int(input())
cg=[[False]*n for _ in range(n)]
for _ in range(mg):
    u,v=map(int,input().split())
    u-=1; v-=1
    cg[u][v]=cg[v][u]=True

mh=int(input())
ch=[[False]*n for _ in range(n)]
for _ in range(mh):
    u,v=map(int,input().split())
    u-=1; v-=1
    ch[u][v]=ch[v][u]=True

a=[]
for i in range(n-1):
    ai=list(map(int,input().split()))
    a.append([0]*(i+1)+ai)  #探索しやすくするためにダミー０追加


ans=10**10
for p in permutations(range(n)):    #cgを固定、全パターン探索
    ansp=0
    for i in range(n-1):
        for j in range(i+1,n):
            if (cg[p[i]][p[j]] and not ch[i][j]) or (not cg[p[i]][p[j]] and ch[i][j]):  #cgを固定し、chとXOR
                ansp+=a[i][j]
    ans=min(ans,ansp)

print(ans)