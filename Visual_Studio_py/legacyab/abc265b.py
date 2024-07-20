n,m,t=map(int,input().split())
a=list(map(int,input().split()))

b=[0 for _ in range(n)]         # ボーナスをlen(n)で管理
for i in range(m):
    xi,yi=map(int,input().split())
    b[xi-1]=yi

for i in range(n-1):
    if t-a[i]<=0:               # a[i]よりtが小さいとダメ
        print('No')
        exit()
    t=t-a[i]+b[i+1]             # 移動先のマスがボーナスだったら+
    # print(t)
print('Yes')