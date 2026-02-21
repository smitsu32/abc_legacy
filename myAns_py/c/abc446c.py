from collections import deque

t=int(input())

for _ in range(t):
    n,d=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    
    q=deque()
    for i in range(n):
        for _ in range(a[i]):
            q.append(i)
        for _ in range(b[i]):
            q.popleft()
        
        while q and q[0]<=i-d:
            q.popleft()
    
    print(len(q))