from bisect import bisect_left,bisect_right

n=int(input())
aa=list(map(int,input().split()))
a=sorted(aa,reverse=True)
c=[0]*(n+1)
for i in range(n):
    c[i+1]=c[i]+a[i]

a,c=a[::-1],c[::-1] #二分探索は昇順リストで
ans=[]
for i in range(n):
    j=bisect_right(a,aa[i])
    ans.append(c[j])
print(*ans)