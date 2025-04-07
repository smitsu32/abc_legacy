from math import *

n=int(input())
ans=0

# i=a
for i in range(1,61): # 2**60>=10**18
    b=isqrt(n//(2**i)) # 平方根
    ans+=(b+1)//2 # 奇数の数

print(ans)