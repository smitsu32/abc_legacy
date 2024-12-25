# ふれんずさんのやり方で 総和から余剰を引く
n=int(input())
MOD=998244353
ans=(1+n)*n//2

for i in range(1,19):
    if n>=10**i:
        ans-=9*10**(i-1) * (n-(10**i-1))
    else:
        break

print(ans%MOD)