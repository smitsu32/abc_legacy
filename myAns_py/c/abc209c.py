n=int(input())
c=list(map(int,input().split()))
c.sort()
MOD=1000000007

ans=1
for i in range(n):
    ans*=c[i]-i
    ans%=MOD

print(ans%MOD)