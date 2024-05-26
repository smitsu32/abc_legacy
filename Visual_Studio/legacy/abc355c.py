# ABC355C ビンゴは何回目？
n,t=map(int,input().split())
a=list(map(int,input().split()))

b,c=[0]*n,[0]*n
sl,rsl=0,0

# 12
# 34
# 無条件で2回目でクリアなので...
if n==2:
    exit(print(2))

for i in range(t):
    b[(a[i]-1)%n]+=1
    c[(a[i]-1)//n]+=1
    
    if b[(a[i]-1)%n]==n or c[(a[i]-1)//n]==n:
        exit(print(i+1))
    # 123
    # 456
    # 789
    # 右下がりは0,4,8の右(n+1で割ったあまり)、右上がりは2,4,6の右(n-1..)
    # ただし右上がりは8と0除く(a[i]=n**2, a[i]=1)
    if a[i]%(n+1)==1: 
        sl+=1
    if a[i]%(n-1)==1 and a[i]!=n**2 and a[i]!=1:
        rsl+=1
    
    if sl==n or rsl==n:
        exit(print(i+1))

print(-1)