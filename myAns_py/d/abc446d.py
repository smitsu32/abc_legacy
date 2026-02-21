from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))

dp=defaultdict(int)
ans=0

for i in range(n):
    # 長さは (-1の数までの長さ) + 1
    dp[a[i]]=dp[a[i]-1]+1
    ans=max(ans,dp[i])

print(ans)