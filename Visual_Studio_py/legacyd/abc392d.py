from collections import defaultdict
from itertools import combinations

n=int(input())
KA=[]
for _ in range(n):
    k,*a=map(int,input().split())
    d=defaultdict(int)
    for i in a:
        d[i]+=1
    KA.append((k,d))

ans=0
for (ki,ai),(kj,aj) in combinations(KA,2):
    ansi=0
    for a,k in ai.items():
        if a in aj:
            ansi+=k*aj[a]
    
    ansi/=ki*kj
    ans=max(ans,ansi)

print(ans)