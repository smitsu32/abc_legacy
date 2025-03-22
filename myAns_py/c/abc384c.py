from itertools import combinations
from bisect import bisect_right,bisect_left

a=list(map(int,input().split()))
al='ABCDE'
t=[]
for r in range(1,len(al)+1):
    for i in combinations(al,r):
        t.append(''.join(i))
t.sort()
ans=[]
ansind=[]
for i in t:
    n=len(i)
    ansi=0
    for j in range(n):
        if i[j] in al:
            temp=ord(i[j])-65
            ansi+=a[temp]
    
    if len(ans)==0:
        ans.append(ansi)
        ansind.append(i)
        continue
    
    pos=bisect_left(ans,ansi)
    ansind.insert(pos,i)
    ans.insert(pos,ansi)

ansind=ansind[::-1]
ans=ans[::-1]
for i in range(len(ansind)):
    print(ansind[i])