n,m=map(int,input().split())

k,x=[],[]
for i in range(m):
    kxi=list(map(int,input().split()))
    x.append(kxi[1:])

c=[[0 for _ in range(n)]for _ in range(n)]      # 参照注意

for i in range(m):
    for j in range(len(x[i])):
        for k in range(len(x[i])):
            c[x[i][j]-1][x[i][k]-1]+=1

for j in range(n):
    for k in range(n):
        if c[j][k]==0:
            print('No')
            exit()

print('Yes')