n,m=map(int,input().split())
a=list(map(int,input().split()))

s=[0]*n
now=1
nowi=a[0]-1

for i in range(m):
    ai=a[i]-1
    s[ai]+=1
    if s[ai]>now:
        now=s[ai]
        nowi=ai
    elif s[ai]==now:
        if ai<nowi:         # 若い番号ならnowを変更
            nowi=ai
    print(nowi+1)