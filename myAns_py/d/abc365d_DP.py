n=int(input())
S=input()
INF=10**9

# i回目にr,s,p出したときの勝ち数
dp=[[0,0,0] for _ in range(n+1)]

for i in range(n):
    r,s,p=0,0,0
    if S[i]=='R':
        p=1 #勝ち
        s=-INF #負け(ドボン)
    elif S[i]=='S':
        r=1
        p=-INF
    else:
        s=1
        r=-INF
    
    dp[i+1][0]=max(dp[i][1]+r,dp[i][2]+r)
    dp[i+1][1]=max(dp[i][0]+s,dp[i][2]+s)
    dp[i+1][2]=max(dp[i][0]+p,dp[i][1]+p)

print(max(dp[-1]))