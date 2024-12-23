n,x=map(int,input().split())
A,B=[0]*n,[0]*n
for i in range(n):
    A[i],B[i]=map(int,input().split())

# dp[i][j]: i回ジャンプを行った時点で座標jの位置にいるのが可能か
dp=[[False]*(x+1) for _ in range(n+1)]
dp[0][0]=True

for i in range(n):
    for j in range(x+1):
            if dp[i][j]:
                if j+A[i]<=x:
                    dp[i+1][j+A[i]]=True
                if j+B[i]<=x:
                    dp[i+1][j+B[i]]=True
# print(dp)
if dp[n][x]:
    print('Yes')
else:
    print('No')