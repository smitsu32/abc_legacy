n,t=input().split()
n=int(n)

def c(s,t):
    k,l,a=0,0,0
    if len(s)>len(t):
        return c(t,s)
    if len(s)<len(t)-1:
        return False
    while len(s)>k:
        if s[k]==t[l]:
            k+=1; l+=1
        else:
            a+=1; l+=1
            if len(s)==len(t):
                k+=1
            if a>1:
                return False
    return True


ans=[]
for i in range(n):
    s=input()
    
    if c(s,t):
        ans.append(i+1)

print(len(ans))
print(*ans)