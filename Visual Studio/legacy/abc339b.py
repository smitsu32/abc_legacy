#ABC339B Langton's Takahashi グリッド上での時計周り移動実装

# c:時計, ac:反時計
def c(a,b): a,b=-b,a; return a,b
def ac(a,b): a,b=b,-a; return a,b

h,w,n=map(int,input().split())
# 2次元リスト h行w列が '.'
g=[['.' for _ in range(w)] for _ in range(h)]

# dx,dyで方向管理  dx->row, dy->col
## 行数(w)->列数(h)と選択されるため g[y][x]
x,y,dx,dy=0,0,0,-1
for _ in range(n):
    if g[y][x]=='.':
        g[y][x]='#'
        dx,dy=c(dx,dy)
        x+=dx; y+=dy
    else:
        g[y][x]='.'
        dx,dy=ac(dx,dy)
        x+=dx; y+=dy 
    #if->else g[y][x]のオーバーフロー防止
    x%=w; y%=h

for i in range(h):
    print(*g[i],sep='')
    
## めも　関数のreturnは一旦別変数に格納する
# e,d=c(a,b)