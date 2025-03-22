from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))

s=defaultdict(int)

for i in range(n):
    s[a[i]]+=1

ans=0
for i,j in s.items():   # s[i]=j
    ans+=j//2

print(ans)