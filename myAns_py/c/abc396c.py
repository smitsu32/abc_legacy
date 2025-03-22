n,m=map(int,input().split())
b=list(map(int,input().split()))
w=list(map(int,input().split()))

b.sort()
b=b[::-1]
w.sort()
w=w[::-1]

# s,t:黒白の累積和、maxt:iまでの白の累積和の最大値
s,t=[0]*(n+1),[0]*(m+1)
maxt=[0]*(m+1)

for i in range(n):
    s[i+1]=s[i]+b[i]
for i in range(m):
    t[i+1]=t[i]+w[i]
    maxt[i+1]=max(maxt[i],t[i+1])

ans=0
for i in range(n+1): #何もカウントしない[0]も含む
    if i<m:
        ans=max(ans,s[i]+maxt[i]) # maxt:0~m
    else:
        ans=max(ans,s[i]+maxt[m])

print(ans)