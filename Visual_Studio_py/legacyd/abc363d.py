n=int(input())

if n==1:
    print(0)
    exit()
n-=1
# 個数の規則性 9,9,90,90,900,...

for i in range(n):
    if n<=2*9*10**i:
        if n<=9*10**i:  #奇数番目
            t=10**i+n-1
            ans=str(t)+str(t)[:-1][::-1]
        else:
            n-=9*10**i
            t=10**i+n-1
            ans=str(t)+str(t)[::-1] #偶数番目
        print(ans)
        exit()
    else:
        n-=2*9*10**i