#ABC355b cにaの要素が連続しているか？
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort(); b.sort()
c=a+b
c.sort()

if n==1: exit(print('No'))

for i in range(n+m-1):
    for j in range(n-1):
        if c[i]==a[j] and c[i+1]==a[j+1]: exit(print('Yes'))
print('No')