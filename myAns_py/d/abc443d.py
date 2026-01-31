t=int(input())
for _ in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    
    ans=[0]*n # 最小値+1を両方向に展開したリスト
    ans[0]=r[0]
    
    # ->
    for i in range(1,n):
        ans[i]=min(r[i],ans[i-1]+1)
        
    # <-
    for i in range(n-2,-1,-1):
        ans[i]=min(ans[i],ans[i+1]+1)
    
    num=0
    for i in range(n):
        num+=r[i]-ans[i]
    
    print(num)