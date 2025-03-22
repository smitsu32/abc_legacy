n,s=map(int,input().split())
a=list(map(int,input().split()))
b=sum(a)

s%=b
if s==0:
    print('Yes')
    exit()

a+=a
S=[a[0]]*2*n
for i in range(1,2*n):
    S[i]=S[i-1]+a[i]

i,j=0,0
while i<n and j<2*n:
    diff=S[j]-S[i]
    if diff==s:
        print('Yes')
        exit()
    elif diff>s:
        i+=1
        j=max(j,i)
    else:
        j+=1

print('No')