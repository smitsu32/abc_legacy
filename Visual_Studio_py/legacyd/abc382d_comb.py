from itertools import combinations_with_replacement

n,m=map(int,input().split())
m-=10*(n-1)

ans=[]
for i in combinations_with_replacement(range(1,m+1),n):
    ans.append(i)

ans.sort()
print(len(ans))
for i in ans:
    for j in range(len(i)):
        print(i[j]+10*j,end=' ')
    print()