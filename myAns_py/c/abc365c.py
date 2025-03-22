from bisect import bisect_left
n,m=map(int,input().split())
a=sorted(list(map(int,input().split())), reverse=True)
b=sum(a)

if b<=m:
    print('infinite')
    exit()
elif n>m:
    print(0)
    exit()

l,r=0,m
while True:
    if l>r:
        l-=1
        break
    
    c=(l+r)//2
    t=sum(min(i,c) for i in a)
    
    if t<=m:
        l=c+1
    else:
        r=c-1

print(l)