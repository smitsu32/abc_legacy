from collections import defaultdict
q=int(input())

d=defaultdict(int)

for i in range(q):
    ab=input().split()
    # print(d)
    if len(ab)==2:
        a,b=int(ab[0]),int(ab[1])
        if a==1:
            d[b]+=1
        elif a==2:
            d[b]-=1
            if d[b]==0:
                del d[b]
    else:
        print(len(d))