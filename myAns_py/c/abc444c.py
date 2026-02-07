def checka(x):
    if len(x)<=1:
        return True
    elif len(x)%2==1:
        return False
    
    c=x[0]+x[-1]
    for i in range(len(x)//2):
        if x[i]+x[-i-1]!=c:
            return False
    return True

def checkb(x):
    if len(x)%2==1:
        return False
    
    c=a[-1]
    for i in range(len(x)//2):
        if x[i]+x[-i-1]!=c:
            return False
    return True


n=int(input())
a=sorted(list(map(int,input().split())))

if len(a)==1:
    print(*a)
    exit()

b=[]
for i in range(n):
    if a[i]!=a[-1]:
        b.append(a[i])

ans=[]
if len(set(a))==1:
    ans.append(a[-1])
elif checkb(b):
    ans.append(a[-1])
if checka(a):
    ans.append(a[0]+a[-1])
print(*ans)