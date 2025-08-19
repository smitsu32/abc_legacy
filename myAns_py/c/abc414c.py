a=int(input())
n=int(input())
m=len(str(n))

def check(i,a):
    num=[]
    while i>0:
        num.append(i%a)
        i//=a
    
    if num==num[::-1]:
        return True
    else:
        return False

ans=0
for l in range(1,10**6):
    ls=str(l)
    d1=int(ls+ls[::-1])
    if d1<=n and check(d1,a):
        ans+=d1
    
    d2=int(ls+ls[:-1][::-1])
    if d2<=n and check(d2,a):
        ans+=d2
    elif d2>n:
        break

print(ans)