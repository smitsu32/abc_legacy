from collections import deque

n=int(input())
T,K,A=[],[],[]
for i in range(n):
    tka=list(map(int,input().split()))
    T.append(tka[0])
    A.append(tka[2:]) #入力は独立させないとRE

d=deque()
d.append(n)
visit=set()
visit.add(n)

ans=T[n-1]
while d:
    t=d.popleft()
    for i in A[t-1]:
        if i not in visit:
            visit.add(i)
            d.append(i)
            ans+=T[i-1]

print(ans)