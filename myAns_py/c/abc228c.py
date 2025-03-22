n,k=map(int,input().split())
a=[]
for i in range(n):
    p=list(map(int,input().split()))
    a.append(sum(p))

b=sorted(a,reverse=True)
s=b[k-1]

for i in range(n):
    if a[i]+300>=s:
        print('Yes')
    else:
        print('No')
