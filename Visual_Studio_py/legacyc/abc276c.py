n=int(input())
p=list(map(int,input().split()))

for i in range(n-2,-1,-1):
    if p[i]>p[i+1]:
        for d in range(1,n):        # p[i]との差
            for k in range(i+1,n):  # 後半を見て差が等しいなら
                if p[i]-d==p[k]:
                    t=p[i]; p[i]=p[k]; p[k]=t   # 入れ替えて
                    a=p[:i+1]
                    b=p[i+1:]
                    b.sort(reverse=True)        # 大きい順に
                    print(*(a+b))               
                    exit()

# p: 9 8 6 5 10 3 1 2 4 7   最後から見て > に変わるところまで
# a: 9 8 6 5 10 2           3に一番近い小さい数字に変える
# b:              7 4 3 1
