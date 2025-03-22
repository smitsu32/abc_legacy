n,m=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(n)]

c=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        c[i][j]=b[i][j]-b[0][0]
        if (b[i][j]-1)//7!=(b[i][0]-1)//7: # 7 8 9 :NG
            print('No')
            exit()

d=[]
for i in range(n):
    di=[]
    for j in range(m):
        di.append(7*i+j)
    d.append(di)

if c==d:
    print('Yes')
else:
    print('No')