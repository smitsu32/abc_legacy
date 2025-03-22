from sortedcontainers import SortedList

q=int(input())
a=SortedList()
c=0
for _ in range(q):
    que=list(map(int,input().split()))
    if len(que)==1:
        b=a.pop(0)
        print(b+c)
    else:
        if que[0]==1:
            a.add(que[1]-c)
        else:
            c+=que[1]