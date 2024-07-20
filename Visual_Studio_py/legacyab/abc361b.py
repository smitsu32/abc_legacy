a=list(map(int,input().split()))
g=list(map(int,input().split()))

x=max(a[0],g[0])<min(a[3],g[3])     # 交差条件
y=max(a[1],g[1])<min(a[4],g[4])
z=max(a[2],g[2])<min(a[5],g[5])

if x and y and z:
    print('Yes')
else:
    print('No')