# ABC323B o判定並べ替え
n=int(input())
ans=[]
for _ in range(n):
    s=input()
    ansi=0
    for i in range(n):
        if s[i]=='o':
            ansi+=1
    ans.append(ansi)

anss=sorted(ans,reverse=True)
aa=[]
for i in range(n):
    for j in range(n):
        if anss[i]==ans[j] and not j+1 in aa:
            aa.append(j+1)
            break

print(*aa)