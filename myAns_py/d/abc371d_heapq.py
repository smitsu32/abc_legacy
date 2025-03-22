from heapq import heappop,heappush,heapify

n=int(input())
h=list(map(int,input().split()))
h=h[::-1]

q=[] # 見えるビルリスト
heapify(q)

ans=[]
for i in range(n):  #最後からみる
    ans.append(len(q))  #見える数を出力
    
    heappush(q,h[i])    #今のビルを見えるリストに追加
    while q[0]<h[i]:    #もし今のビルより小さいなら消す（高いビルjが存在してしまう）
        heappop(q)
    # print(q)

ans=ans[::-1]
print(*ans)