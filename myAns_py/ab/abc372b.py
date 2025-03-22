m=int(input())
t=[]

a=0
while True:
    if 3**a<=m:
        a+=1
    else:
        break
for i in range(a):
    t.append(m//(3**(a-i)))
    m%=3**(a-i)
t.append(m)
t=t[::-1]

ans=[]
for i in range(len(t)):
    while t[i]>0:
        ans.append(i)
        t[i]-=1

print(len(ans))
print(*ans)