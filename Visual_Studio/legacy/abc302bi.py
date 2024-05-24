# ABC302b ６方向５マスずつ探索
## 重要
h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
dir=((1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)) # 第2,4象限ナナメ忘れ注意

ans='snuke'
for i in range(h):          #重要な探索方法
    for j in range(w):
        for dx,dy in dir:       # dirの値を順にdx,dyに代入
            frag=True           # dirとkの2階分脱出するためfragを用いる
            for k in range(5):
                newx=j+dx*k; newy=i+dy*k
                if not 0<=newx<w or not 0<=newy<h:  #newx,yがgrid範囲内か？
                    frag=False; break
                if s[newy][newx]!=ans[k]:           #ポインタ先は'snuke'か？
                    frag=False; break
            if frag:
                [print(i+dy*l+1,j+dx*l+1)for l in range(5)]; exit()