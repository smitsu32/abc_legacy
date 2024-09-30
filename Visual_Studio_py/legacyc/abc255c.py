x,a,d,n=map(int,input().split())
if d<0: # 公差が負だとうまくいかない
    a=a+d*(n-1)
    d*=-1
mins=min(a,a+d*(n-1))
maxs=max(a,a+d*(n-1))

if x<=mins:
    print(mins-x)
elif maxs<=x:
    print(x-maxs)
else:
    if d==0:
        print(0)
    else:
        x-=mins
        print(min(x%d, d-(x%d)))
