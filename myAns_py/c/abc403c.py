n,m,q=map(int,input().split())

ok=[set() for _ in range(n+1)]
allok=set()

for _ in range(q):
    qu=input().split()
    if qu[0]=="1":
        x,y=int(qu[1]),int(qu[2])
        ok[x].add(y)
    elif qu[0]=='2':
        x=int(qu[1])
        allok.add(x)
    else:
        x,y=int(qu[1]),int(qu[2])
        if y in ok[x] or x in allok:
            print("Yes")
        else:
            print("No")