from bisect import bisect_left,bisect_right

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[]
ind=[]
now=10**7
for i in range(n):
    if a[i]<now:
        now=a[i]
        c.append(a[i])
        ind.append(i+1)
ind=ind[::-1]
c=c[::-1]
# print(c,ind)
for i in range(m):
    ans=bisect_right(c,b[i])
    if ans==0:
        print(-1)
        continue
    print(ind[ans-1])