#ABC299b 色&値 最強カードは？
mp=lambda: map(int,input().split())
lmp=lambda: list(map(int,input().split()))

n,t=mp()
c=lmp(); r=lmp()

ans=0; ansp=0
for i in range(n):
    if c[i]==t and r[i]>ans:
        ans=r[i]; ansp=i+1

if ansp==0:
    ans=r[0]; ansp=1
    for i in range(n):
        if c[i]==c[0] and r[i]>ans:
            ans=r[i]; ansp=i+1

print(ansp)