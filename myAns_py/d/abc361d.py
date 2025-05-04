from collections import deque

n=int(input())
s=list(input())
t=list(input())

if s.count('B')!=t.count('B') or s.count('W')!=t.count('W'):
    print(-1)
    exit()

s+=['.','.']
t+=['.','.']
used=set()
used.add(tuple(s))

d=deque()
d.append([s,0])

while d:
    u,cnt=d.popleft()
    if u==t:
        print(cnt) # BFSのためminが保証
        exit()
    
    for i in range(n+2):
        if u[i]=='.':
            idx=i
            break
    
    for i in range(n+1):
        if u[i]=='.' or u[i+1]=='.':
            continue
        tmp=u[:]
        tmp[i],tmp[i+1],tmp[idx],tmp[idx+1]=tmp[idx],tmp[idx+1],tmp[i],tmp[i+1]
        if tuple(tmp) not in used:
            used.add(tuple(tmp))
            d.append([tmp,cnt+1])

print(-1)