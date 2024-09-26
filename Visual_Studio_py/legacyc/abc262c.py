n=int(input())
a=list(map(int,input().split()))

ans=0
for i in range(n):
    if a[i]==i+1:
        ans+=1

ans=ans*(ans-1)//2

for i in range(n):
    j=a[i]
    if i+1<j and a[j-1]==i+1:
        ans+=1

print(ans)