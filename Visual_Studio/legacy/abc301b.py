# ABC301b 数列を階段状に
n=int(input())
a=list(map(int,input().split()))

b=[]
for i in range(n-1):
    b.append(a[i])
    if a[i]+1<a[i+1]:
        for j in range(a[i]+1,a[i+1]): b.append(j)
    elif a[i]>a[i+1]+1:
        for j in range(a[i]-1,a[i+1],-1): b.append(j)
print(*b,a[n-1])