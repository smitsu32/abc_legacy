s=input()
n=len(s)
t='chokudai'
m=len(t)
MOD=1000000007

# dp[i][j]: i番目にt[j]までを選べるのは何通り？
dp=[[0]*(m+1) for _ in range(n+1)]
dp[0][0]=1

for i in range(n):
    for j in range(m+1):
        dp[i+1][j]=dp[i][j] #ひきつぎ
        if j>=1 and s[i]==t[j-1]:
            dp[i+1][j]=(dp[i][j]+dp[i][j-1])%MOD

print(dp[n][m]%MOD)