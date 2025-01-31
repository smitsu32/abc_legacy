n=int(input())
a=list(map(int,input().split()))

if n==2:
    print('Yes')
    exit()

# a[i+1]/a[i] = a[i+2]/a[i+1] のとき　a[i+1]^2=a[i]a[i+2]
for i in range(n-2):
    if a[i+1]**2!=a[i]*a[i+2]:
        print('No')
        exit()
print('Yes')