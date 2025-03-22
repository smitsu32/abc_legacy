# ABC309B cの合計金額は？
mp=lambda: map(int,input().split())
li=lambda: list(input().split())
n,m=mp()
c=li(); d=li()
p=list(mp())

ans=0
for i in range(n):
        if c[i] in d:
            for j in range(m):
                if c[i]==d[j]:
                    ans+=p[j+1]
        else: ans+=p[0]
print(ans)