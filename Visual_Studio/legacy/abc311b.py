# ABC311B 長方形が全てoとなる最大行数は？
n,d=map(int,input().split())
s=[input() for _ in range(n)]
ans=0

# 10行目のforで oooxとooooがどちらも3と出力されるため 分けて処理
o=['o'*d for _ in range(n)]
if o==s: exit(print(d))

for i in range(d):
    for j in range(d-i):
        frag=True
        for k in range(n):
            if s[k][i+j]!='o': frag=False
        if frag==False: break
    if j>ans:
        ans=j
print(ans)