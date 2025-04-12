n,k=map(int,input().split())
MOD=10**9

a=[1 for _ in range(n+1)] #足す前(a[-1])スタート
now=k # 1*k
for i in range(k,n+1):
    a[i]=now
    now=(now+a[i]-a[i-k])%MOD

print(a[-1])