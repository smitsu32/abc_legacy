n=int(input())
a=list(map(int,input().split()))

imos=[0]*(n+1) #imos法
# 範囲のはじめを+1, おわりの１個後を-1する (n+1は範囲外用)
# [l,r]の範囲を+1する問題に有効
# imos[i]は元から何個プラスになったかを格納する

for i in range(n):
    a[i]+=imos[i] #くれた分を足す
    
    if n-1-i>=a[i]: #あげた分 　 オーバーしたら
        imos[i+1]+=1            #１個後の人から
        imos[i+a[i]+1]-=1       # a[i]人先まであげる
    else:           # オーバーしなかったらただプラスする
        imos[i+1]+=1
        # imos[n]-=1
    a[i]=max(a[i]-(n-1-i),0)
    
    imos[i+1]+=imos[i]          #iさんの分を引継ぎ

print(*a) #,imos)