n,k,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort(reverse=True)

ans=sum(a)
for i in range(n):
    if a[i]>=x:
        t=a[i]//x
        if t<=k:
            ans-=t*x
            a[i]%=x
            k-=t
        else:
            ans-=k*x
            print(ans)
            exit()
# print(ans,k)
a.sort(reverse=True)

for i in range(min(k,n)):
    ans-=a[i]

print(ans)