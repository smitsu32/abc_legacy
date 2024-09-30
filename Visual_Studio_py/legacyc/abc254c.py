n,k=map(int,input().split())
a=list(map(int,input().split()))
c=sorted(a) #O(NlogN)

b=a[:]
for i in range(k):  # b[i::k]はk個おきに複数選べるのでkの%回だけでよい
    b[i::k]=sorted(b[i::k])

if c==b:
    print('Yes')
else:
    print('No')