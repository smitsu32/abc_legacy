import sys
sys.setrecursionlimit(10**6)

n=int(input())
a=list(map(int,input().split()))
used=[False for _ in range(n)]

i=0
for _ in range(n):      # n回ループでiが閉路内に
    i=a[i]-1

ans=[]
while True:
    if used[i]:
        break
    used[i]=True
    i=a[i]-1
    ans.append(a[i])

print(len(ans))
print(*ans)