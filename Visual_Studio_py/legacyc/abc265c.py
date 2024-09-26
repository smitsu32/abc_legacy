h,w=map(int,input().split())
g=[input() for _ in range(h)]

x,y=0,0
s=set()
s.add((0,0))
while True:
    if g[y][x]=='U' and y!=0:
        y-=1
    elif g[y][x]=='D' and y!=h-1:
        y+=1
    elif g[y][x]=='L' and x!=0:
        x-=1
    elif g[y][x]=='R' and x!=w-1:
        x+=1
    else:
        print(y+1,x+1)
        exit()
    
    if (y,x) in s:
        print(-1)
        exit()
    s.add((y,x))
