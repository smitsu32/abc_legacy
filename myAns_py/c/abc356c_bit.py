n,m,k=map(int,input().split())

c,a,r=[],[],[]
for i in range(m):
    ci,*ai,ri=input().split()
    c.append(int(ci))
    a.append(list(map(int,ai)))
    r.append(ri)

# bit全探索, n本の全ての鍵パターンを試す
ans=0
for bit in range(1<<n): # 000,001,010,011,100,101,110,111 どの鍵を使うか(use:1 unuse:0)
    flag=True           # bitは全てのデータセット条件を満たすか？
    
    for i in range(m): # 各データセットでfor
        count=0
        
        for j in a[i]: # aを一個ずつ取り出して
            if bit>>(j-1) & 1 == 1: # 0~n+1のいずれかの数字を２進表記して
                count+=1            # 1の数を数える　(a[i]:1~n+1なのでj-1)
        
        if flag==True:
            if count<k and r[i]=='o': # bitのパターンでは正しい鍵が足りない
                flag=False
            elif count>=k and r[i]=='x': # bitのパターンでは鍵数は足りるが鍵が合わない
                flag=False

    # print(bin(bit),flag)
    
    if flag==True: # bitが全てのデータセットを満たすときただしい
        ans+=1
    
print(ans)