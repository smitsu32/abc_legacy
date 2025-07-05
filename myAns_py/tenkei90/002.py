n=int(input())
if n%2==1:
    exit()

ans=[]

for bit in range(1<<n):
    use=[-1]*n
    for i in range(n):
        if bit&1<<i:
            use[i]=1
    if use.count(1) != n//2:
        continue
    
    now=0
    f=True
    ansn=[]
    for i in range(n):
        if use[i]==1:
            now+=1
            ansn.append('(')
        else:
            if now==0:
                f=False
                break
            else:
                now-=1
                ansn.append(')')
    
    if f and ansn!=[]:
        ans.append(''.join(ansn))

ans.sort()
for i in ans:
    print(i)