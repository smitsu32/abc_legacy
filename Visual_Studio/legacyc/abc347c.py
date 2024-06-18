n,a,b=map(int,input().split())
d=list(map(int,input().split()))
w=a+b

for i in range(n):
    d[i]=d[i]%w
d=sorted(list(set(d)))

l=len(d)
# print(d)

dif=d[0]+w-d[l-1]

for i in range(l-1):
    difi=d[i+1]-d[i]
    dif=max(dif,difi)

if dif>b: print('Yes')      # もし差の最大(dif<=w)が平日をまたいだら
else: print('No')