n,w=map(int,input().split())
X=[[] for _ in range(w)]
cnt=[0]*w  #各列何個？

for i in range(n):
    x,y=map(int,input().split())
    x-=1; y-=1
    X[x].append((y,i+1)) #何秒か
    cnt[x]+=1

ans=[-1]*(n+1) #消える時間
for i in range(min(cnt)): #縦に順に見て，消える行ぶんfor
    t=0
    for j in range(w):
        t=max(X[j][i][0],t)  # X[j][i][0]: i列で最も遅く落ちてくる時間
    t+=1  #消えた0.5秒後をみたいから+1
    for j in range(w):
        ans[X[j][i][1]]=t
# print(ans)

q=int(input())
for _ in range(q):
    t,a=map(int,input().split())
    # a-=1
    if ans[a]==-1 or ans[a]>t:
        print('Yes')
    else:
        print('No')