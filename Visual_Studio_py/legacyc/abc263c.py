from itertools import combinations

n,m=map(int,input().split())
a=[i+1 for i in range(m)]

for i in list(combinations(a,n)):
    print(*i)