n=int(input())
a=list(map(int,input().split()))
a.sort()

cnt=0
r=n
# 両端から尺取り法
for i in range(n):
    r=max(r,i+1)
    while r>i+1 and a[r-1]+a[i]>=10**8:
        r-=1
    cnt+=n-r #rより大きい数

ans=0
for i in range(n):
    ans+=a[i]*(n-1)   # 1+sum[1:] + 2+sum[2:]+...

ans-=10**8*cnt
print(ans)