# ABC325B 時間繰り返し判定
n=int(input())
w=[]; x=[]
for i in range(n):
    wi,xi=map(int,input().split())
    w.append(wi); x.append(xi)

ans,ansi=0,0
for i in range(24):
    for j in range(n):
        if 9<= (x[j]+i)%24 <= 17:
            ansi+=w[j]
    if ansi>ans:
        ans=ansi
    ansi=0

print(ans)