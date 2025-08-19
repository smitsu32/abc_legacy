from collections import deque
q=int(input())

d=deque()
for _ in range(q):
    qu=input().split()
    if qu[0] == '1':
        c,x=int(qu[1]), int(qu[2])
        d.append((c,x))
    else:
        k=int(qu[1])
        ans=0
        while True:
            c,x=d.popleft()
            if c>k:
                ans+=k*x
                d.appendleft((c-k, x))
                print(ans)
                break
            elif c==k:
                ans+=k*x
                print(ans)
                break
            else:
                ans+=c*x
                k-=c