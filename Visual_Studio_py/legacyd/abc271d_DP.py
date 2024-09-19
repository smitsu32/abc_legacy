n,s=map(int,input().split())

# dp[i][j]: i番目の入力時に文字数S=jは存在するか？
#          存在するなら表裏を記録
dp=[['']*(s+1) for _ in range(n+1)]
dp[0][0]='@'    # 判定上の仮文字

for i in range(n):
    a,b=map(int,input().split())
    for j in range(s+1):    # i,jが存在するときS+=a, S+=bに記録
        if dp[i][j]:
            if j+a<s+1: # 範囲内なら
                dp[i+1][j+a]=dp[i][j]+'H'
            if j+b<s+1:
                dp[i+1][j+b]=dp[i][j]+'T'

if dp[-1][-1]:
    print('Yes')
    print(dp[-1][-1][1:])   # '@'削除
else:
    print('No')