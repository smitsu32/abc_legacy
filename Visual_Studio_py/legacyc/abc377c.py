n,m=map(int,input().split())
end=set()
vec=[[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]

a,b=[0]*m,[0]*m
for i in range(m):
    a[i],b[i]=map(int,input().split())
    end.add((a[i],b[i]))

for i in range(m):
    ai,bi=a[i],b[i]
    for x,y in vec:
        if 1<=bi+y<=n and 1<=ai+x<=n:
            end.add((ai+x,bi+y))
# print(sorted(list(end)))
print(n*n-len(end))