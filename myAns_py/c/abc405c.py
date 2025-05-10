n=int(input())
a=list(map(int,input().split()))

b=a[::-1]
c=[0]
now=0
for i in range(n):
    now+=b[i]
    c.append(now)
c=c[::-1]
# print(c)

ans=0
for i in range(n-1):
    ans+=a[i]*c[i+1]
    # print(ans)
    
print(ans)