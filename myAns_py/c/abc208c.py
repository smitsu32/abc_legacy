n,k=map(int,input().split())
a=list(map(int,input().split()))

b=[]
for i,ai in enumerate(a):
    b.append([i,ai])
b.sort(key=lambda x: x[1])

ans=[k//n]*n
k%=n

for i in range(k):
    ind,cnt=b[i]
    ans[ind]+=1

print(*ans,sep='\n')