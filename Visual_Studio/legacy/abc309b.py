# ABC309b グリッドの外側を時計回りに
n=int(input())
a=[list(input()) for _ in range(n)]
b=[[a[j][i] for i in range(n)]for j in range(n)]

for i in range(n-1):
    b[0][i+1]=a[0][i]; b[-1][i]=a[-1][i+1]
    b[i][0]=a[i+1][0]; b[i+1][-1]=a[i][-1]
for i in range(n): print(*b[i],sep='')
# # ↓ 全セル時計周り
# #     ６行目~最後 #反転

# # 全部左右に移動
# # ただし中央で向きが反転
# # ->-> . 
# # ->-> .
# # . <-<-
# # . <-<-

# for i in range(n//2):
#     for j in range(n-1):
#         b[i][j+1]=a[i][j]
#         b[-i-1][j]=a[-i-1][j+1]

# # o...↓
# # oo.↓o
# # oo.oo
# # o↑.oo　o:上下の数が代入されるところ
# # ↑...o  <-の1,2列目を考えると18行目に

# for i in range(n//2):
#     for j in range(n-1-2*i):
#         b[j+i][i]=a[j+1+i][i]
#         b[j+1+i][-i-1]=a[j+i][-i-1]
# print('')

# for i in range(n):
#     print(*b[i],sep='')