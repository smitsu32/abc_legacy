n=int(input())
X,Y=[0]*n,[0]*n
for i in range(n):
    X[i],Y[i]=map(int,input().split())

INF=10**9

def a(x1,y1,x2,y2):
    if x1!=x2:
        return (y2-y1)/(x2-x1)
    else:
        return INF

ans=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ij=a(X[i],Y[i],X[j],Y[j])
            jk=a(X[j],Y[j],X[k],Y[k])
            ki=a(X[k],Y[k],X[i],Y[i])
            if ij==jk==ki:
                continue
            else:
                ans+=1
                # print(i+1,j+1,k+1)

print(ans)