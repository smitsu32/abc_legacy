n,k=map(int,input().split())
a=list(map(int,input().split()))
suma=sum(a)

ok,ng=0,10**100  # maxに注意
while abs(ok-ng)>1: 
    mid=(ok+ng)//2

    g=0 # 合計人数
    for i in range(n):
        if a[i]>mid:
            g+=mid
        else:
            g+=a[i]
    
    ansi=mid*k  # マス目
    if g>=ansi: # = 必須
        ok=mid
    else:
        ng=mid
print(ok)

# 表を考える(ユーザ解説)