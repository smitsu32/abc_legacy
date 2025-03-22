from itertools import permutations

n,k=map(int,input().split())
s=list(input())

## ないとTLE!!!
if len(set(s))==n:
    ans=1
    for i in range(1,n+1):
        ans*=i
    
    print(ans)
    exit()

ans=0
for l in set(permutations(s)):
    f=False
    for i in range(n-k+1):
        t=l[i:i+k]
        if t==t[::-1]:
            f=True
            break
    if f==False:
        ans+=1

print(ans)
