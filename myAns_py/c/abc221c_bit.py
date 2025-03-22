n=list(input())
n=sorted(n,reverse=True)
m=len(n)

ans=0
for bit in range(1,1<<m-1):
    use=[False]*m
    for i in range(m):
        if bit&(1<<i):
            use[i]=True
            
    a,b='',''
    for i in range(m):
        if use[i]:
            a+=n[i]
        else:
            b+=n[i]
    ans=max(ans,int(a)*int(b))

print(ans)