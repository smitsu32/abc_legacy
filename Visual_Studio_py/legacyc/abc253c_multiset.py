from collections import defaultdict
from heapq import heappush,heappop

q=int(input())
c=defaultdict(int)  # 要素の数をcount

# heapq: minがO(1)
maxheap,minheap=[],[]

for _ in range(q):
    a=list(map(int,input().split()))
    if a[0]==1:
        c[a[1]]+=1
        heappush(maxheap,-a[1]) # maxは*-1する
        heappush(minheap,a[1])
    elif a[0]==2:
        c[a[1]]-=a[2]
    else:
        while c[-maxheap[0]]<=0:
            heappop(maxheap)
        while c[minheap[0]]<=0:
            heappop(minheap)
        print(-maxheap[0]-minheap[0])