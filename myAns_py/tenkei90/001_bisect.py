n,L=map(int,input().split())
k=int(input())
a=list(map(int,input().split()))

def check(x):
    cnt,now=0,0
    for i in range(n):
        if a[i]-now>=x:
            cnt+=1
            now=a[i]
    if L-now>=x:
        cnt+=1
    return cnt

l,r=-1,L+1
while abs(l-r)>1:
    mid=(l+r)//2
    if check(mid)>=k+1:
        l=mid
    else:
        r=mid

print(l)