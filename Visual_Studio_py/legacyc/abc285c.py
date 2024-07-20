s=list(input())
s.reverse()

# 26進数とみなせる
ans=0
for i in range(len(s)):
    ans+=(ord(s[i])-64)*26**i

print(ans)