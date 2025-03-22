from itertools import product

n,k=map(int,input().split())
r=list(map(int,input().split()))

ans=list(product(*[range(1,i+1) for i in r]))

for i in ans:
    if sum(i)%k==0:
        print(" ".join(map(str,i)))