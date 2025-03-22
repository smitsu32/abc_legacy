n,m,K=map(int,input().split())
MOD=998244353

#i+1個めの数はi個めまでで決まる>状態遷移>DP
#dp[i][j]:i番目までで和jとなる個数
dp=[[0]*(K+1) for _ in range(n+1)]
dp[0][0]=1

for i in range(n):
    for j in range(K):
        for k in range(1,m+1):
            if j+k<=K:
                dp[i+1][j+k]+=dp[i][j]

print(sum(dp[-1])%MOD)