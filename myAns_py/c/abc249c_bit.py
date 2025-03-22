n,k=map(int,input().split())
s=[input() for _ in range(n)]

ans=0
for bit in range(1<<n):
    
    use=[False]*n
    for i in range(n):
        if bit&(1<<i):
            use[i]=True
    
    d=[0]*26
    for i in range(n):
        flag=[0]*26
        if use[i]:
            for j in s[i]:
                flag[ord(j)-97]=1
            
            for j in range(26):
                if flag[j]==1:
                    d[j]+=1
    # print(use,d)
    
    pos=[0]*26
    for i in range(26):
        pos[d[i]]+=1
    
    ans=max(ans,pos[k])

print(ans)