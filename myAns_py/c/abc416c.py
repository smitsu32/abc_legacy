from itertools import product

n,k,x=map(int,input().split())
s=[]
for i in range(n):
    s.append(input())


ans=[]
for l in product(range(n), repeat=k):
    ansi=''
    for i in l:
        ansi+=s[i]
    ans.append(ansi)

ans.sort()
print(ans[x-1])