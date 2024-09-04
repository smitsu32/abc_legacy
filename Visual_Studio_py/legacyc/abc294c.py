n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c,d,e=[],[],[]
for i in range(n):
    d.append([a[i],i])
for j in range(m):
    d.append([b[j],j+10**10])   # bのindexを隔離して管理

e=sorted(c+d,key=lambda x: x[0])

ansa,ansb=[0]*n,[0]*m
for i in range(n+m):
    if e[i][1]<10**10:          # a,bに分離
        ansa[e[i][1]]=i+1
    else:
        ansb[e[i][1]-10**10]=i+1

print(*ansa)
print(*ansb)