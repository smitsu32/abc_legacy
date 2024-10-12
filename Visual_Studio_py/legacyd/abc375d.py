from collections import defaultdict

s=input()
n=len(s)

if n<3:
    print(0)
    exit()

d=defaultdict(list)
e=defaultdict(int)
f=defaultdict(list)
for i in range(n):
    e[s[i]]+=1
    d[s[i]].append(i)
    if not f[s[i]]:
        f[s[i]].append(0)
        f[s[i]].append(i)
    else:
        t=f[s[i]][-1]
        f[s[i]].append(t+i)

ans=0
for i in e:
    if e[i]<=1:
        continue
    
    for j in range(e[i]):
        ans+=j*d[i][j]-f[i][j]
    ans-=0.5*e[i]*(e[i]-1)
print(int(ans))
