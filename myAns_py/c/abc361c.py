n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=a[:]

# print(b)
s=n-k
if s<=1:
    print(0)
    exit()

# i~i+sの最大値と最小値だけ分かればいいから...
# k+1回繰り返して最小値を出力
ans=10**9
for i in range(k+1):
    d=b[i+s-1]-b[i]
    ans=min(d,ans)
print(ans)