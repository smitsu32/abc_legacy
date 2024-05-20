# aとの距離が最小となるx(l<=x<=r)を出力
def mp(): return map(int,input().split())
n,l,r=mp()
a=list(mp())

p=[]
for i in range(n):
    if l<=a[i]<=r:
        p.append(a[i])
    elif a[i]<l:
        p.append(l)
    else:
        p.append(r)

print(*p)