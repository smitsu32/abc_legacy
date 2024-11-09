from collections import deque

q=int(input())

t,le=0,0
d=deque()

for i in range(q):
    query=input().split()
    if len(query)==1:
        d.append(t)
    else:
        if query[0]=='2':
            t+=int(query[1])
        else:
            ans=0
            while d and t-d[0]>=int(query[1]):
                ans+=1
                d.popleft()
            print(ans)
    # print(d,t,le)