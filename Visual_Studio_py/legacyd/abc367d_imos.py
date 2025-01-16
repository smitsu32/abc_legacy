n,m=map(int,input().split())
a=list(map(int,input().split()))

b=[0]
now=0
for i in range(2*n):
    now+=a[i%n]
    b.append(now%m)

div=[0]*m #あまりごとに記録 imosみたいな
ans=0
for i in range(1,n):
    div[b[i]%m]+=1
ans+=div[b[0]]

for i in range(1,n):
    div[b[n+i-1]]+=1
    div[b[i]]-=1 #1(i+1)~3(n-1)を2(i+1+1)~4(n)に
    ans+=div[b[i]]
    # print(div,ans,b[i])

print(ans)