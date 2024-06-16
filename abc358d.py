# 尺取り法
n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))

ans=0
l=0
for i in range(n):
    if a[i]>=b[l]:
        ans+=a[i]
        l+=1
        if l==m:
            break

if ans!=0 and l==m: print(ans)
else: print(-1)