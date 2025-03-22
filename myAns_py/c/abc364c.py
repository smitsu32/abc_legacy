n,x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=list(zip(a,b))
d=[]
for p,q in c:
    d.append([p,q])

e=sorted(d,key=lambda x: x[0], reverse=True)
f=sorted(d,key=lambda x: x[1], reverse=True)

# print(e,f)
ans1=0
s1=0
for i in range(n):
    if s1+e[i][0]<=x:
        ans1+=1
        s1+=e[i][0]
    else:
        ans1+=1
        break

s2=0
ans2=0
for i in range(n):
    if s2+f[i][1]<=y:
        ans2+=1
        s2+=f[i][1]
    else:
        ans2+=1
        break

print(min(ans1,ans2))