from math import log2
n=int(input())
a=list(map(int,input().split()))

b=[a[0]]
for i in range(1,n):
    b.append(a[i])
    if len(b)==1: continue
    if b[-2]!=b[-1]: continue
    
    while True: # マージはb[-2]==b[-1]の限り続いていく
        del b[-1]
        b[-1]+=1
        if len(b)==1: break
        if b[-2]!=b[-1]: break

print(len(b))