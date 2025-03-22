n,m=map(int,input().split())

wmin=10**10
xyc=[]
for i in range(m):
    x,y,c=input().split()
    xyc.append([int(x),int(y),c])
xyc.sort()

for i in range(m):
    x,y,c=xyc[i]
    if c=='W':
        wmin=min(wmin,y) #whiteが最大値になるように
    else:
        if y>=wmin: #blackが大きいとダメ
            print('No')
            exit()
print('Yes')