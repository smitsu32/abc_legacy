n=int(input())
s=[list(input()) for i in range(n)]
t=[['.']*n for i in range(n)]
#グリッドのドーナツ状の左上点について min(x,y)%4でsからの回転回数を決める
# ドーナツの外から1>2>3>0>1>2>3...回時計回りに回転
for i in range(n):
    for j in range(n):
        a=min(i,j,n-i-1,n-j-1)
        x,y=i,j
        a=(a+1)%4 #最外が１回だから
        for _ in range(a):
            x,y=y,n-x-1 #回転
        t[x][y]=s[i][j]

for i in t:
    print(*i,sep='')