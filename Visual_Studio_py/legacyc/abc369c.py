n=int(input())
a=list(map(int,input().split()))
dif=[]
for i in range(n-1):
    dif.append(a[i+1]-a[i])

c=0
r=0
ans=n
ansi=0
for i in range(n-1):            # i:0以外一緒なので、i-1で処理
    if i!=0:
        if dif[i-1]==dif[i]:    
            ansi+=1             # sigmaにするために+1して毎回足す
        else:
            ansi=1              # 初期化
    else:
        ansi=1
    ans+=ansi                   # sigma
print(ans)