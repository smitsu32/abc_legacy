n,a,b=map(int,input().split())
p,q,r,s=map(int,input().split())

# (a,b)を通り、X状の位置を#にする
# Input1: (3,2)から斜め四方向に黒を延ばす
# p<=i<=q+1, r<=j<=s+1のグリッドを出力

for i in range(p,q+1):
    ans=['.']*(s-r+1)
    for j in range(r,s+1):
        if i==j+(a-b) or i==-j+(a+b):   # ij平面で直線の式(j=(+-ai)+(b-(+-a))をたてる
            ans[j-r]='#'
    print(''.join(ans))

#   # . . . # j
#   . # . # .
#   . . # . # b
#   . # . # .
#   # . . . #
#   i   a
# (a,b)=(3,3)