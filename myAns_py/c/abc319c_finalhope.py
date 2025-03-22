from itertools import permutations

c=[0]*9
c[0],c[1],c[2]=map(int,input().split())
c[3],c[4],c[5]=map(int,input().split())
c[6],c[7],c[8]=map(int,input().split())

ans=0
al=9*8*7*6*5*4*3*2

z=[i for i in range(9)] #[0,1,2,3,4,5,6,7,8]
for p in list(permutations(z)): #(0,1,2,3,4,5,6,7,8)の全パターン試す
    r=[[] for _ in range(3)]
    col=[[] for _ in range(3)]
    cr1,cr2=[],[]
    
    for pi in p:    # 1パターン試す
        r[pi//3].append(c[pi])  #行
        col[pi%3].append(c[pi])   #列
        if pi in (0,4,8):       #右下
            cr1.append(c[pi])
        if pi in (2,4,6):       #左下
            cr2.append(c[pi])
    flag=True
    for i in range(3):
        if r[i][0]==r[i][1] or col[i][0]==col[i][1]: #最初二つに見た数が同じなら
            flag=False
    if cr1[0]==cr1[1] or cr2[0]==cr2[1]:
        flag=False
    
    if flag:
        ans+=1

pp=ans/al
print(f'{pp:.15f}') # 有効数字は15桁くらいまでOK