from collections import *
n,q=map(int,input().split())

cnt=[1]*n
now=[i for i in range(n)]
ans=0
for _  in range(q):
    query=input().split()
    if query[0]=='1':
        p,h=int(query[1])-1,int(query[2])-1
        cnt[now[p]]-=1
        cnt[h]+=1
        if cnt[now[p]]==1:
            ans-=1
        if cnt[h]==2:
            ans+=1
        now[p]=h
    else:
        print(ans)