from itertools import permutations

n,m=map(int,input().split())
s=[input() for _ in range(n)]

for si in permutations(s):
    flag=True
    for i in range(n-1):
        c=0
        for j in range(m):
            if si[i][j]!=si[i+1][j]:
                c+=1
                if c>=2:
                    flag=False
                    break
    if flag:
        print('Yes')
        exit()

print('No')