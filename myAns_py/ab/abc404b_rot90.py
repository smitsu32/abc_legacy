n=int(input())
s=[list(input()) for _ in range(n)]
t=[list(input()) for _ in range(n)]

ans=10**18
for i in range(4):
    ansI=i
    for j in range(n):
        for k in range(n):
            if s[j][k]!=t[j][k]:
                ansI+=1
    ans=min(ans,ansI)
    
    s=[list(row) for row in zip(*s[::-1])]

print(ans)