#ABC303b 隣り合わない組み合わせの数は？
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(m)]

b=[[0 for _ in range(51)]for _ in range(51)]
s=0
for i in range(1,n): s+=i

for i in range(n-1):
    for j in range(m):
        c,d=max(a[j][i],a[j][i+1]),min(a[j][i],a[j][i+1])
        b[c-1][d-1]=1

sb=0
for i in range(51):
    for j in range(51):
        if b[j][i]==1: sb+=1

print(s-sb)