n=int(input())
a=list(map(int,input().split()))

ind,ans=0,0
for i in range(n//2,n):
    if a[ind]*2<=a[i]:  # 尺取り法みたいな 半分から後と前を探索して鏡餅を順につくる
        ind+=1
        ans+=1

print(ans)