#ABC261A ２色の重複部分の出力

l1,r1,l2,r2 = map(int,input().split())

if r1 < l2 or r2 < l1:  #重複せず
    print(0)
else:
    print(min(r2,r1)-max(l2,l1))    #右のminと左のmaxを比較