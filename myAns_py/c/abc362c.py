n=int(input())
l,r=[],[]
x=[]
for i in range(n):
    li,ri=map(int,input().split())
    l.append(li)
    r.append(ri)
    x.append(li)

s=sum(x)

if s>0:
    print('No')
    exit()

for i in range(n):
        d=min(-s,r[i]-l[i]) #s->0かr[i]だけ増えるか
        s+=d
        x[i]+=d

if s==0:
    print('Yes')
    print(*x)
else:
    print('No')