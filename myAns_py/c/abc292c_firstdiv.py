n=int(input())

ans=0
for i in range(1,n):    #2重だがO(N*sqrt(N))
    ab,cd=i,n-i     # AB+CDをAB,CDに分割
    
    ansab,anscd=0,0
    for j in range(1,int(ab**0.5)+1):   # ABが整数
        if ab%j==0:
            ansab+=1
            if j*j!=ab:         # jがABの平方根でないとき
                ansab+=1
    for k in range(1,int(cd**0.5)+1):   # CDが整数
        if cd%k==0:
            anscd+=1
            if k*k!=cd:
                anscd+=1
    
    ans+=ansab*anscd

print(ans)