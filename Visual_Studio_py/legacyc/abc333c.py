n=int(input())
a=[]
m='1'
for i in range(12):
    a.append(int(m))
    m=str(m)+'1'

s=set()
for i in range(12):
    for j in range(12):
        for k in range(12):
            s.add(a[i]+a[j]+a[k])

s=sorted(s)

print(s[n-1])