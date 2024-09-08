from itertools import combinations

s=[input() for _ in range(9)]

p=set()
for i in range(9):
    for j in range(9):
        if s[i][j]=='#':
            p.add((j,i))

per=list(combinations(p,4))

ans=0
for ij in per:
    d=[]
    for (i,j) in combinations([0,1,2,3],2):
        d.append((ij[i][0]-ij[j][0])**2+(ij[i][1]-ij[j][1])**2)
    d.sort()
    if d[0]==d[1]==d[2]==d[3] and d[4]==d[5] and 2*d[0]==d[4]:
        ans+=1

print(ans)