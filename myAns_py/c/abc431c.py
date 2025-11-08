n,m,k=map(int,input().split())
h=list(map(int,input().split()))
b=list(map(int,input().split()))
h.sort()
b.sort()

i,j=0,0
ans=0
while j<m and i<n:
    if h[i]<=b[j]:
        i+=1
        ans+=1
        j+=1
    else:
        j+=1

if ans>=k:
    print('Yes')
else:
    print('No')