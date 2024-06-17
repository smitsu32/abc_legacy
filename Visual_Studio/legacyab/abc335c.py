ips=lambda: input().split()
ip=lambda: input()
ii=lambda: int(input())
mp=lambda: map(int,input().split())
lmp=lambda: list(map(int,input().split()))

vec=[[1,0],[-1,0],[0,1],[0,-1]]

n,q=mp()

x,y=[i+1 for i in range(n)],[0 for _ in range(n)]
x.reverse()
nowdx,nowdy=1,0


for i in range(q):
    a,b=ips()
    a=int(a)
    
    if a==1:
        if b=='R':
            nowdx+=vec[0][0]
            nowdy+=vec[0][1]
        elif b=='L':
            nowdx+=vec[1][0]
            nowdy+=vec[1][1]
        elif b=='U':
            nowdx+=vec[2][0]
            nowdy+=vec[2][1]
        else:
            nowdx+=vec[3][0]
            nowdy+=vec[3][1]
        x.append(nowdx)
        y.append(nowdy)
        # print(x,y)

    elif a==2:
        b=int(b)
        print(x[-b],y[-b])