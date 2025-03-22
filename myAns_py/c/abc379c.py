n,m=map(int,input().split())
X=list(map(int,input().split()))    #入力順任意！！！！！
A=list(map(int,input().split()))

xa=[]
for i in range(m):
    xa.append([X[i],A[i]])
xa.sort(key=lambda x:x[0])
x,a=[],[]
for i in range(m):
    x.append(xa[i][0])
    a.append(xa[i][1])

if sum(a)!=n:
    print(-1)
    exit()
    
f=False
for i in range(m):
    if x[i]==1:
        f=True
        break
if f==False:
    print(-1)
    exit()

ans=0

for i in range(m-1):
    t=a[i]-(x[i+1]-x[i])
    if t<0:
        print(-1)
        exit()
    
    a[i]-=t
    a[i+1]+=t
    ans+=t*(x[i+1]-x[i])
# print(x,a,ans)
for i in range(m):
    ans+=(1+a[i]-1)*(a[i]-1)//2

print(ans)