# ありえる最小の値 -> 二分探索
# import bisect

n,m=map(int,input().split())
l=list(map(int,input().split()))
for i in range(n):
    l[i]+=1

a,b=0,sum(l)    # a:NG b:OK

# 二分探索
def bi(c):
    nowl,row=0,1
    for i in range(n):
        if l[i]>c:          # 1単語の長さにも満たないとき(c:NG)
            return False
        
        if nowl+l[i]<=c:    # 同一行に足すとき
            nowl+=l[i]
        else:               # 改行のとき
            nowl=l[i]
            row+=1
    if row<=m:              # 列が少ない時(c:OK)
        return True
    else:                   # 列が多すぎるとき(c:NG)
        return False

while abs(a-b)>1:
    c=(a+b)//2
    if bi(c):               # c:OK->OKをcまで下げる
        b=c
    else:                   # c:NG->NGをcまで上げる
        a=c

print(b-1)          # OKmin-1を出力(行頭の１文字削除(解説参照))