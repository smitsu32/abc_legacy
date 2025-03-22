n=int(input())
a=[[['']*n for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=list(map(int,input().split()))
# print(a)

s=[[[0]*(n+1) for _ in range(n+1)] for _ in range(n+1)] #3次元累積和

for i in range(n):
    for j in range(n):
        for k in range(n):
            # +1が2つをたす、1つをひく、０こをたす
            s[i+1][j+1][k+1] = s[i+1][j+1][k]+s[i+1][j][k+1]+s[i][j+1][k+1] -s[i][j+1][k]-s[i+1][j][k]-s[i][j][k+1] +s[i][j][k] +a[i][j][k]
# print(s)

q=int(input())
for i in range(q):
    lx,rx,ly,ry,lz,rz=map(int,input().split())
    lx-=1 #左側は-1
    ly-=1
    lz-=1
    ans = s[rx][ry][rz] -s[lx][ry][rz]-s[rx][ly][rz]-s[rx][ry][lz] +s[lx][ly][rz]+s[lx][ry][lz]+s[rx][ly][lz] -s[lx][ly][lz]
    print(ans)