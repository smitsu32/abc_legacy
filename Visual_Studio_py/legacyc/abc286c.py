n,a,b=map(int,input().split())
s=input()

ans=b*n
ansa=-a
for i in range(n):  # 普通に全探索
    t=s[i:]+s[:i]
    ansa+=a
    
    ansb=0
    for j in range(n//2):
        if t[j]!=t[n-j-1]:
            ansb+=b
    ans=min(ans,ansa+ansb)
print(ans)