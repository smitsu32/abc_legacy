sx,sy=map(int,input().split())
tx,ty=map(int,input().split())

# タイルの左側にする
sx-=(sy+sx)%2; tx-=(ty+tx)%2          # x=偶,y=偶 or x=奇,y=奇　が左タイル(x+y=偶)

# タイルの対称性から
# (sx,sy)=(0,0) (tx,ty)=(tx-sx,ty-sy)->絶対値　と平行移動できる
tx-=sx; ty-=sy
sx,sy=0,0
tx=abs(tx); ty=abs(ty)

# 基本縦移動だけ
# txがでかい時はtyに(tx-ty)//2をたす必要あり
print(ty+max(0,tx-ty)//2)