n=int(input())
p=list(map(int,input().split()))

for i in range(n-2,-1,-1):
    if p[i]>p[i+1]:
        t=i
        break

now=-1
s=-1
for i in range(n-1,t-1,-1):
    if p[t]>p[i] and p[i]>now:
        now=p[i]
        s=i

p[s],p[t]=p[t],p[s]
# print(p,s,t)
a,b=p[:t+1],p[t+1:]
b.sort()
print(*a,*b[::-1])