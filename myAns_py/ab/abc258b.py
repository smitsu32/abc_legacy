n=int(input())
a=[list(input()) for _ in range(n)]
vec=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

ans=0
for i in range(n):
    for j in range(n):
        for ki,kj in vec:
            ansk=[a[i][j]]
            for l in range(1,n):
                ansk.append(a[(i+l*ki)%n][(j+l*kj)%n])
            ans=max(ans,int(''.join(ansk)))
print(ans)