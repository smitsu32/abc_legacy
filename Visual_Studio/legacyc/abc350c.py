n=int(input())
a=list(map(int,input().split()))

ans=[]
for i in range(n-1):
    while i+1!=a[i]:        # i<jより 312>213>123 [0]=1よりend
        ans.append([i+1,a[i]])
        temp=a[a[i]-1]; a[a[i]-1]=a[i]; a[i]=temp 

print(len(ans))

for i in ans:
    print(*i)