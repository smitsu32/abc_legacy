from bisect import bisect_left,bisect_right

n=int(input())
x,p=list(map(int,input().split())),list(map(int,input().split()))

pc=[0]
pnow=0
for i in range(n):
    pnow+=p[i]
    pc.append(pnow)

q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    lc=bisect_left(x,l)
    rc=bisect_right(x,r)
    print(pc[rc]-pc[lc])