# ABC318B 合計面積？
n=int(input())
a,b,c,d=[],[],[],[]
for i in range(n):
    ai,bi,ci,di=map(int,input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

x=max(b)-min(a); y=max(d)-min(c)
grid=[[1 for _ in range(y)] for _ in range(x)]

for i in range(n):
    for j in range()