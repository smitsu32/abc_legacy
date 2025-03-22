n=int(input())

g=[['.']*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        d=min(i,j,n-i-1,n-j-1)
        if d%2==0:
            g[i][j]='#'

for i in g:
    print(*i,sep='')