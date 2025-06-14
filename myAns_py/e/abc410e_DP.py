n,h,m=map(int,input().split())
a=[]
for _ in range(n):
    ai,bi=map(int,input().split())
    a.append((ai,bi))

dp=[[-1]*(h+1) for _ in range(n+1)] # 敵i、体力jのときの魔力値
dp[0][h]=m
for i in range(n):
    for j in range(h+1): # 現体力
        hi,mi=a[i]
        if dp[i][j]==-1:
            continue
        
        if j>=hi: # 体力で倒す
            dp[i+1][j-hi]=max(dp[i+1][j-hi], dp[i][j])
        
        if dp[i][j]>=mi: # 魔力で倒す
            dp[i+1][j]=max(dp[i+1][j], dp[i][j]-mi)
# print(dp)

ans=0
for i in range(n+1):
    for j in range(h+1):
        if dp[i][j]!=-1:
            ans=max(ans,i)
            break

print(ans)
