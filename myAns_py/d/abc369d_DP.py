n=int(input())
a=list(map(int,input().split()))

INF=10**18
dp=[[-INF,-INF] for _ in range(n+1)]    # dp[][0]:偶数 dp[][1]:奇数
dp[0][0]=0

#DP
for i in range(1,n+1):
    dp[i][0]=max(dp[i-1][0],dp[i-1][1]+a[i-1]*2)    # 偶数後に追加なし or 奇数後+a[偶数]
    dp[i][1]=max(dp[i-1][1],dp[i-1][0]+a[i-1])      # 奇数後に追加なし or 偶数後+a[奇数]

# DP_even[i] = max(DP_even[i-1],DP_odd[i-1] + 2*a[i])
# DP_odd[i] = max(DP_odd[i-1],DP_even[i-1] + a[i])

print(max(dp[n][0],dp[n][1]))