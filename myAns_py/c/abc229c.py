n,w=map(int,input().split())
a=[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append([ai,bi])
a.sort(key=lambda x:x[0],reverse=True)

now=0
ans=0
for i in range(n):
    if now+a[i][1]<=w:
        ans+=a[i][0]*a[i][1]
        now+=a[i][1]
    else:
        ans+=a[i][0]*(w-now)
        # print(ans,a[i],now)
        print(ans)
        exit()
    # print(ans,a[i],now)

print(ans)