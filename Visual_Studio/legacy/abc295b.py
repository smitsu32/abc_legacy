# ABC295B グリッド x+yの絶対値が1~9のとき#を.に
r,c=map(int,input().split())
b=[list(input()) for _ in range(r)]

for i in range(c):
    for j in range(r):
        if b[j][i]!='.' and b[j][i]!='#':
            temp=int(b[j][i]) 
            b[j][i]='.'
            
            # マンハッタン距離(x,yの直線距離の合計がtemp以内) '#'->'.'
            for k in range(c):
                for l in range(r):
                        if abs(j-l)+abs(i-k)<=temp and b[l][k]=='#': 
                            b[l][k]='.'

# ２次元リスト出力方法
# for i in range(r):
#     print(*b[i],sep='')
for i in b: print(''.join(i))