n=int(input())

x=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append([a,1])
    x.append([a+b,-1])
x.sort()
# print(x)

now=0
ans=[0]*(n+1)
for i in range(len(x)-1):
    now+=x[i][1]
    ans[now]+=x[i+1][0]-x[i][0]

print(*ans[1:])