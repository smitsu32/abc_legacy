from collections import *

q=int(input())
offset=0
d=deque()
for _ in range(q):
    qi=input().split()
    if qi[0]=='1':
        if len(d)==0:
            d.append([qi[1],0])
            continue
        
        now=d[-1]
        d.append([int(qi[1]),int(now[0])+int(now[1])])
    elif qi[0]=='2':
        d.popleft()
        if len(d)!=0:
            offset=d[0][1]
        else:
            offset=0
    else:
        print(d[int(qi[1])-1][1]-offset)