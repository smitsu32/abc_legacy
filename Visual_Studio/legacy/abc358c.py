ips=lambda: input().split()
ip=lambda: input()
iip=lambda: int(input())
mp=lambda: map(int,input().split())
lmp=lambda: list(map(int,input().split()))

n,m=mp()
a=[]
for i in range(n):
    a.append(input())

# はじめてのbit全探索
ans=n
for bit in range(1<<n):     # 0~2**n-1まで(0000,0001,0010,0011,0100,...,0111)
    use=[False]*n           # 使う行をTrueに
    for i in range(n):      # 0*n-1まで(0,1,2,3)
        if bit & (1<<i):    # nの2進数(bit)と0001->0010->0100->...(i)を比較
            use[i]=True     # 0~n-1について２進数の値を格納(ex. n=4,i=2ならbit=0010->use=[FFTF])
    # print(use)
    ok=[False]*m            # m列についてo->Trueと記録する
    
    for i in range(n):      # use[i]がTrueの行をチェックしてaのi行目j列目が'o'ならok[j]をTrueに上書き
                            # ex. a[xxo, xox,ooo],use=[TTF]ならok=xoo->[FTT]
        if use[i]:
            for j in range(m):
                if a[i][j]=='o':
                    ok[j]=True
    # print(ok)
    if all(ok):
        ans=min(ans,sum(use))

print(ans)