from bisect import bisect_left,bisect_right
n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))

ans=1
for i in range(n):
    b=bisect_left(a,a[i]+m)
    ans=max(ans,b-i)

print(ans)