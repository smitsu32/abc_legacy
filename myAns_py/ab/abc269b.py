# a,b=map(int,input().split())

s=[list(input()) for _ in range(10)]

flag1=False
b=-1
for i in range(10):
    for j in range(10):
        if s[j][i]=='#' and flag1==False:
            c=i+1; a=j+1; flag1=True
        elif s[j][i]=='#' and flag1:       #最終値は上書きで数えればよい
            d=i+1; b=j+1
        
if b==-1:                       # #が1マスのとき
    b=a; d=c
print(a,b); print(c,d)