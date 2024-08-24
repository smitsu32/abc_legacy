# permutations
from itertools import permutations

m=int(input())
s1=list(input()*3)
s2=list(input()*3)
s3=list(input()*3)
s=[s1,s2,s3]

INF=10**9
ans=INF
for p in list(permutations([0,1,2])):
    for i in range(m):
        for j in range(i+1,2*m):
            for k in range(j+1,3*m):
                if s[p[0]][i]==s[p[1]][j]==s[p[2]][k]:
                    ans=min(ans,k)
                    # print(ans)

if ans==INF:
    print(-1)
else:
    print(ans)