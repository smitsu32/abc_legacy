n,m,h,k=map(int,input().split())
s=list(input())
xy=set()
for _ in range(m):
    x,y=map(int,input().split())
    xy.add((x,y))           # in が O(1)

x,y=0,0
for i in range(n):
    if s[i]=='R':
        x+=1
    elif s[i]=='L':
        x-=1
    elif s[i]=='U':
        y+=1
    else:
        y-=1
    h-=1
    
    if h<0:
        print('No')
        exit()
    
    if (x,y) in xy:
        if h<k:
            xy.discard((x,y))
        h=max(k,h)

print('Yes')