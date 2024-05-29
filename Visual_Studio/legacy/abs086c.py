# ABS086c t秒に(xi,yi)が全てOKか?
n=int(input())

xa,ya,tnow=0,0,0
frag=True
for _ in range(n):
    t,x,y=map(int,input().split())
    d=abs(x-xa)+abs(y-ya)
    xa=x; ya=y
    ta=t-tnow; tnow=t
    
    if d>ta or (ta-d)%2==1:
        frag=False
        
if frag: print('Yes')
else: print('No')