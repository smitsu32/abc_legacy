n,l=map(int,input().split())
d=list(map(int,input().split()))

if l%3!=0:
    print(0)
    exit()

s=[0]
now=0
for i in d:
    now=(now+i)%l
    s.append(now)

ss=[0]*l
for i in s:
    ss[i]+=1

ans=0
for i in range(l//3):
    if ss[i]>0 and ss[i+l//3]>0 and ss[i+2*l//3]>0:
        ans+=ss[i]*ss[i+l//3]*ss[i+2*l//3]
print(ans)