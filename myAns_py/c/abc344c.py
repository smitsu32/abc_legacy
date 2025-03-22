def ii():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

n,a=ii(); m,b=ii(); l,c=ii(); q,x=ii()
ch=set()                # set型を使う
for i in range(n):
    for j in range(m):
        for k in range(l):
            ch.add(a[i]+b[j]+c[k])

# ch=list(set(ch))      # 実質ソートなのでO(q^2)となりTLE
                        # ソートしないとforがO(l*m*n*q)となりTLE
for i in range(q):
    if x[i] in ch: print('Yes')
    else: print('No')
