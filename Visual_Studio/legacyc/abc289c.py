n,m=map(int,input().split())
c,a=[],[]
for i in range(m):
    c.append(int(input()))
    a.append(list(map(int,input().split())))
    
ans=0
for bit in range(1<<m):     # 0~2**n-1までbit表記(0000,0001,0010,0011,0100,...,0111)
    use=[False]*m           # 使う行をTrueに(0->False, 1->True)
    for i in range(m):      # 0*n-1まで(0,1,2,3)
        if bit & (1<<i):    # nの2進数(bit)と0001->0010->0100->...(i)を比較
            use[i]=True     # ここまでコピペすればOK(注意:m>20でTLE)
    
    ch=set()                # set..重複を防ぐ
    for i in range(m):      # データセットの中で使うものだけすべての要素をsetに
        if use[i]:
            for j in range(c[i]):
                ch.add(a[i][j])
    if len(ch)==n:          # chに1~nが格納されていたらans +1
        ans+=1

print(ans)