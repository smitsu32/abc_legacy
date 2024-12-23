n=int(input())
s=[list(input()) for _ in range(n)]

def next(i,j):
    for di,dj in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
        miss=0
        if not (0<=i+di*5<n and 0<=j+dj*5<n):
            continue
        
        for k in range(1,6):
            ni,nj=i+di*k,j+dj*k
            if s[ni][nj]=='.':
                miss+=1
        
        if miss<=2:
            return True
    return False

for i in range(n):
    for j in range(n):
        if s[i][j]=='#':
            if next(i,j):
                print('Yes')
                exit(0)
print('No')