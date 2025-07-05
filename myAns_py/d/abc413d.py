t=int(input())

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    b=len(set(a))
    
    if b==1: # 全て同じ値
        print('Yes')
    elif b==2 and min(a.count(a[0]),a.count(-a[0]))==n//2: # 交互
        print('Yes')
    else:
        a.sort(key=lambda x: abs(x)) # 絶対値ソート
        
        f=True
        for i in range(n-2):
            if a[i]*a[i+2]!=a[i+1]**2:
                f=False
                break
        if f:
            print('Yes')
        else:
            print('No')