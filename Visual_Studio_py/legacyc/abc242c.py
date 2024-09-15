n=int(input())
MOD=998244353
dp=[[0]*9 for _ in range(n)]
for i in range(9):
    dp[0][i]=1

for i in range(n-1):
    for j in range(9):
        if j==0:
            dp[i+1][j]=(dp[i][j]+dp[i][j+1])%MOD
        elif j==8:
            dp[i+1][j]=(dp[i][j]+dp[i][j-1])%MOD
        else:
            dp[i+1][j]=(dp[i][j]+dp[i][j-1]+dp[i][j+1])%MOD

print(sum(dp[-1])%MOD)