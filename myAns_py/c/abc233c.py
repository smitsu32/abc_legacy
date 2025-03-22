n,x=map(int,input().split())
l,a=[],[]

for _ in range(n):
    li,*ai=map(int,input().split())
    l.append(li)
    a.append(ai)

ans=0
b=[1]
for i in range(n):
    c=[]
    for j in a[i]:          # aのi行目から1つずつピックアップ
        for k in b:         # bに一行前の総積を格納
            c.append(j*k)   # 前積[k]*a[i][j]
    b=c[:]

ans=b.count(x)
print(ans)