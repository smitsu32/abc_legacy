# ABC320B 回文
s=input()

ans=1
# iから任意の長さのtが回文か判定
## [::-1]は逆順
for i in range(len(s)):
    for j in range(1,len(s)-i):
        t=s[i:i+j+1]
        if t==t[::-1]: ans=max(len(t),ans)

print(ans)