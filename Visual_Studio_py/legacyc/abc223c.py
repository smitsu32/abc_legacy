n=int(input())
a,b=[],[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)

s=0
for i in range(n):
    s+=a[i]/b[i] # s:秒数
s/=2

ans=0 # ans: cm
for i in range(n):
    if a[i]/b[i]<s:
        s-=a[i]/b[i]
        ans+=a[i]
    else:
        ans+=s*b[i]
        print(ans)
        exit()