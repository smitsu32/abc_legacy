from collections import deque

n=int(input())
a=list(map(int,input().split()))
d=deque()

# d(i,j): iが連続j個め
for i in range(n):
    if len(d)==0:
        d.append((a[i],1))
    else:
        if d[-1][0]==a[i]:
            d.append((a[i],d[-1][1]+1))
            if d[-1][1]==a[i]:
                for _ in range(a[i]):
                    d.pop()
        else:
            d.append((a[i],1))
    print(len(d))
    # print(d)