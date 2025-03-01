n,q=map(int,input().split())

invname=[i for i in range(n)] #箱iはもともとなに
pos=[i for i in range(n)] # 鳩aはもともと箱bにいる
name=[i for i in range(n)] #箱iはいまなに

for _ in range(q):
    op=list(map(int,input().split()))
    if op[0]==1:
        a,b=op[1]-1,op[2]-1
        pos[a]=name[b] #bの今の箱番号に更新
    elif op[0]==2:
        a,b=op[1]-1,op[2]-1
        ai,bi=name[a],name[b]
        invname[ai],invname[bi]=invname[bi],invname[ai] #もともと箱a,bだったやつの今の箱番号を入替
        name[a],name[b]=name[b],name[a] #今の位置を入れ替えるだけ
    else:
        a=op[1]-1
        print(invname[pos[a]]+1) #鳩aがいる現在の箱を出力->元々の箱の位置を参照する必要がある
