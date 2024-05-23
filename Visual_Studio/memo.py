n=int(input())
a=[]
c=[]
for i in range(n):
    ai,ci=map(int,input().split())
    a.append(ai)
    c.append(ci)

b=sorted(a)
for i in range(n):
    if
m=[]
for i in range(n):
    flag=False
    for j in range(i+1,n):
        if a[i]<a[j] and c[i]>c[j]:
            flag=True
            continue
    if flag==False:
        m.append(i+1)

print(len(m))
for i in range(len(m)):
    print(m[i],end=' ')