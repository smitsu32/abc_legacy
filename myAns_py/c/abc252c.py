n=int(input())
s=[]
for i in range(n):
    s.append(input()*n)

ans=10**9
for m in range(10):
    push=set()
    for i in range(n):
        for j in range(n*10):
            if int(s[i][j])==m and j not in push:
                push.add(j)
                break
    ans=min(ans,max(push))
print(ans)