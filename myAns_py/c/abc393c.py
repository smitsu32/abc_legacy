n,m=map(int,input().split())

g=set()
ans=0
for i in range(m):
    u,v=map(int,input().split())
    u-=1; v-=1
    if u>v:
        u,v=v,u
    elif u==v:
        ans+=1
        continue
    
    if (u,v) in g:
        ans+=1
    else:
        g.add((u,v))

print(ans)