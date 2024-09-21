n,q=map(int,input().split())
s=list(input())

a=set()
for i in range(n-2):
    if s[i:i+3]==['A','B','C']:
        a.add((i,i+1,i+2))
for _ in range(q):
    x,c=input().split()
    x=int(x)-1
    
    if s[x]==c:
        None
    else:
        a.discard((x,x+1,x+2))
        a.discard((x-1,x,x+1))
        a.discard((x-2,x-1,x))
        s[x]=c # リストにしないとTLE
        if x+2<n:
            if s[x:x+3]==['A','B','C']:
                a.add((x,x+1,x+2))
        if 0<=x-1 and x+1<n:
            if s[x-1:x+2]==['A','B','C']:
                a.add((x-1,x,x+1))
        if 0<=x-2:
            if s[x-2:x+1]==['A','B','C']:
                a.add((x-2,x-1,x))
    print(len(a))