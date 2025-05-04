l,r=map(int,input().split())

def f(r): # r以下のsnake数を返す
    if r==0:
        return 0
    
    d=[]
    while r>0:
        d.append(r%10)
        r//=10
    d=d[::-1]
    
    n=len(d)
    
    ans=0
    ## r=5** なら 500<=r を考える
    for i in range(1,1+n):
        # case1
        if i==n:
            ans+=1
            break
        
        # case2
        ans+=d[0]**(n-i-1)*min(d[0],d[i]) #i+1桁目以降　* <d[i](d[0])によりrを超えない
        if d[0]<=d[i]: # snakeじゃない → ↑で考慮済
            break
    
    ## r=5** なら r<4**を考える
    for i in range(n):
        if i==0: # 最大桁 → 最大桁数d[0]未満のみ
            mx=d[0]-1
        else: #それより桁数が小さい数 → snake数なら全部足せる
            mx=9

        for j in range(1,mx+1):
            ans+=j**(n-i-1) # OKな数字*桁数

    return ans

snake=f(r)-f(l-1) # snake数はl~rのsnake数-f(r-1)で求まる
print(snake)