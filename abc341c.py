h,w,n=map(int,input().split())
t=input()
s=[]
for i in range(h):
    s.append(list(input()))

m=[]
for i in range(n):                  # vecに合わせてtを変換
    if t[i]=='L':  m.append(0)
    elif t[i]=='R':  m.append(1)
    elif t[i]=='U':  m.append(2)
    elif t[i]=='D':  m.append(3)

ans=0
vec=[[-1,0],[1,0],[0,-1],[0,1]]     #vecで管理すると楽～
for i in range(w):
    for j in range(h):
        if s[j][i]!='.':
            continue
        
        x,y=i,j
        flag=True
        for k in range(n):
            dx,dy=vec[m[k]][0],vec[m[k]][1]     # １マスごとの移動を格納
            x+=dx; y+=dy
            if x<=-1 or w<=x or y<=-1 or h<=y:  # 範囲外
                flag=False; break
            if s[y][x]!='.':                    # 海
                flag=False; break
        if flag:
            ans+=1
print(ans)