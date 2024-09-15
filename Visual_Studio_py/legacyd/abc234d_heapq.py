from heapq import heappop,heappush,heapify #min,maxはやい

n,k=map(int,input().split())
a=list(map(int,input().split()))

b=a[:k]
heapify(b)
ans=heappop(b)
print(ans)

for i in range(k,n):
    heappush(b,max(a[i],ans)) #a[i]<ansなら答えは前と同じ、ans挿入, 逆なら1index進む,a[i]挿入
    ans=heappop(b)
    print(ans)