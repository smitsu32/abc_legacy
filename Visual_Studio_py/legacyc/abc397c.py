from collections import defaultdict

n=int(input())
a=list(map(int,input().split()))

#正順と負順を合わせる
L=[]
ll=defaultdict(int)
sl=0
for i in range(n):
    if not ll[a[i]]:
        ll[a[i]]=1
        sl+=1
    L.append(sl)

R=[0] #L=maxのとき
b=a[::-1]
rr=defaultdict(int)
sr=0
for i in range(n):
    if not rr[b[i]]:
        rr[b[i]]=1
        sr+=1
    R.append(sr)
R=R[::-1]

ans=0
for i in range(n):
    ans=max(ans,L[i]+R[i+1]) #iまでとi+1からの和
print(ans)