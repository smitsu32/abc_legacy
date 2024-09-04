n,q=map(int,input().split())

s=set()
c,ans=0,0
for _ in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        c+=1
        s.add(c)
    elif a[0]==2:
        x=a[1]
        s.discard(x)
    else:
        for i in range(n):      # ansで最小値管理(set型でminを取るとTLE)
            if not ans in s:
                ans+=1
            else:
                break
        print(ans)