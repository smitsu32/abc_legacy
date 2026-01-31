n,t=map(int,input().split())
a=list(map(int,input().split()))

if n==0:
    print(t)
    exit()

ans=a[0]
last=a[0]

for i in range(1,n):
    if a[i]>last+100:
        ans+=a[i]-last-100
        last=a[i]

if t>last+100:
    ans+=t-last-100

print(ans)