n=int(input())
q=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans,jmin=0,10**6
for i in range(10**6+1):    #ax+by=q x=iに固定
    if max(q)-i*max(a)<0: break
    
    for qi,ai,bi in zip(q,a,b):
        if qi-i*ai<0:
            break
        
        if bi!=0: 
            j=(qi-i*ai)//bi
            jmin=min(j,jmin)
    else:                       # break回避
        ans=max(ans,i+jmin)
print(ans)