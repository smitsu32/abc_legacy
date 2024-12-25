n,s=map(int,input().split())
A,B=[0]*n,[0]*n
for i in range(n):
    A[i],B[i]=map(int,input().split())

dp=[[False]*(s+1) for _ in range(n+1)]
dp[0][0]=True

for i in range(n):
    a,b=A[i],B[i]
    for j in range(s+1):
        if dp[i][j]:
            if j+a<=s:
                dp[i+1][j+a]=True
            if j+b<=s:
                dp[i+1][j+b]=True

A,B=A[::-1],B[::-1]

#探索順の復元（逆からたどる）
if dp[n][s]:
    print('Yes')
    ans=['']*n
    for i in range(n):
        if s>=A[i] and dp[n-1-i][s-A[i]]:
            ans[i]='H'
            s-=A[i] #sを減らしてjの代わりに
        else:
            ans[i]='T'
            s-=B[i]
    print(*ans[::-1],sep='')
    
else:
    print('No')