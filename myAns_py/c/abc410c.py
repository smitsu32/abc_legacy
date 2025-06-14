n,q=map(int,input().split())
a=[i for i in range(1,n+1)]

offset=0
for _ in range(q):
    qu=list(map(int,input().split()))
    if qu[0]==1:
        p,x=qu[1],qu[2]
        a[(p+offset-1)%n]=x
    elif qu[0]==2:
        p=qu[1]
        print(a[(p+offset-1)%n])
    else:
        offset=(offset+qu[1])%n