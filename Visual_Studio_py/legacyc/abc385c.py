n=int(input())
h=list(map(int,input().split()))

seth=set(h)
if len(seth)==n:
    print(1)
    exit(0)
elif len(seth)==1:
    print(n)
    exit(0)

ans=0
for r in range(1,n//2+1):
    for start in range(r):
        ansi=0
        temp=h[start]
        for i in range(start,n,r):
            if h[i]==temp:
                ansi+=1
            else:
                ans=max(ansi,ans)
                ansi=1
                temp=h[i]
        ans=max(ansi,ans)
        # print(h[start:n:r],start,r,ansi)
print(ans)