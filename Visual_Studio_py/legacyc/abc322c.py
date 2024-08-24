n,m=map(int,input().split())
a=list(map(int,input().split()))

j=0
for i in range(1,n+1):
    if a[j]>=i:
        print(a[j]-i)
    else:
        while a[j]<i:
            j+=1
        print(a[j]-i)
