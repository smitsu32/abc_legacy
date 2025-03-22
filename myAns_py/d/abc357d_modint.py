n=int(input())
MOD=998244353

# (与式) = n(1+10^k+10^2k+...+10^(n-1)k) = n(10^nk-1)/(10^k-1))
k=len(str(n)) #要素数
num=n*(pow(10,n*k,MOD)-1)%MOD

## 分母を逆元にして割り算を掛け算に(MOD演算ではやらないといけない)
div=pow(10,k,MOD)-1
div=pow(div,MOD-2,MOD)

print(num*div%MOD)