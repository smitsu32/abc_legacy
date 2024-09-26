n,q=map(int,input().split())
s=list(input())

a=0
for _ in range(q):
    t,x=map(int,input().split())
    if t==1:
        a+=x
    else:
        print(s[(x-a-1)%n]) #x:1-indexed