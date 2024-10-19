n,q=map(int,input().split())
ans=0
l,r=0,1

for i in range(q):
    h,t=input().split()
    t=int(t)-1
    
    if h=='R':
        if r==t: continue
        
        if l<r<t or t<r<l or r<t<l or l<t<r:
            ans+=abs(t-r)
        else:
            ans+=n-abs(t-r)
        r=t
    else:
        if l==t: continue
        
        if r<l<t or t<l<r or l<t<r or r<t<l:
            ans+=abs(t-l)
        else:
            ans+=n-abs(t-l)
        l=t
print(ans)