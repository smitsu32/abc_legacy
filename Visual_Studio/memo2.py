# ABC320B 回文
s=input()

ans=0
for i in range(1,len(s)+1):
    for j in range(i,len(s)+1):
        t=s[i:j]; u=t[::-1]
        if t==u: ans=len(t)
print(ans)