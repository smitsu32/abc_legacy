h,w=map(int,input().split())
c=[input() for _ in range(h)]
next=[(1,1),(-1,1),(1,-1),(-1,-1)]
def cross(x,y):
    for i in range(1,min(h,w)):
        count=0
        for dx,dy in next:
            newx=x+dx*i
            newy=y+dy*i
            if 0<=newx<h and 0<=newy<w and c[newx][newy]=='#':
                count+=1
        if count!=4:
            return i-1      #その回は入らない

ans=[0]*min(h,w)
for i in range(h):
    for j in range(w):
        if c[i][j]=='#':
            ansi=cross(i,j)
            if ansi>0:
                ans[ansi-1]+=1      # １以上を-1のindexに保存
print(*ans)