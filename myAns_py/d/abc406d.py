h,w,n=map(int,input().split())
row=[[] for _ in range(h+1)]
col=[[] for _ in range(w+1)]

# used x.y
ux=[False]*(h+1)
uy=[False]*(w+1)

# trash
used=[False]*n

for i in range(n):
    x,y=map(int,input().split())
    row[x].append(i)
    col[y].append(i)

# ごみは1回しか処理されないから実行時間はO(N+Q)
q=int(input())
for _ in range(q):
    q=list(map(int,input().split()))
    if q[0]==1:
        x=q[1]
        if ux[x]:
            print(0)
            continue
        
        ans=0
        for i in row[x]: #行を探索
            if not used[i]: #列を判定
                ans+=1
                used[i]=True
        ux[x]=True
        print(ans)
    
    else:
        y=q[1]
        if uy[y]:
            print(0)
            continue
        
        ans=0
        for i in col[y]: #列を探索
            if not used[i]: #行を判定
                ans+=1
                used[i]=True
        uy[y]=True
        print(ans)