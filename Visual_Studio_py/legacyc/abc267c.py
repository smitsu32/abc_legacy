n,m=map(int,input().split())
a=list(map(int,input().split()))

t=[0]
now=0
for i in range(n):
    now+=a[i]
    t.append(now)

s=[]
now=0
for i in range(m):
    now+=(i+1)*a[i]
s.append(now)

for i in range(n-m):
    s.append(s[i]-(t[i+m]-t[i]-m*a[i+m]))   # s:答え t:累積和 S0,S1をA[i]*iの形で筆算風に書くとわかりやすい

print(max(s))