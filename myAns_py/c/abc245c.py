n,k=map(int,input().split())
INF=float('inf')

a=list(map(int,input().split()))
b=list(map(int,input().split()))

dp=[[-INF, -INF] for _ in range(n)]
dp[0][0],dp[0][1]=a[0],b[0]

for i in range(n-1):
    ai,bi=-INF,-INF
    if abs(a[i+1]-dp[i][0])<=k or abs(a[i+1]-dp[i][1])<=k:
        dp[i+1][0]=a[i+1]
    if abs(b[i+1]-dp[i][1])<=k or abs(b[i+1]-dp[i][0])<=k:
        dp[i+1][1]=b[i+1]

if max(dp[-1])>-INF:
    print('Yes')
else:
    print('No')