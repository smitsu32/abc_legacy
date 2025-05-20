from bisect import bisect_left as bileft
n=int(input())
a=sorted(list(map(int,input().split())))

r=10**8
count=0

for i in range(n):
    ci=bileft(a,r-a[i])     #a=[1 50000001 50000002 50000003],i=1ならci=1, count=3 (後で1引く)
    count+=n-ci
    
    if 2*a[i]>=r:           # 同数重複削除
        count-=1 # 50000000+50000000が重複している 1回

count=count//2              # countは２倍カウントしている[1 50000001][50000001,1]
print( (n-1)*sum(a) - count*r )     #(x+yの合計)　-　(10**8より大きい個数)*10**8

# x+y >= 10^8 のとき、f()=x+y-10^8
# x+y < 10^8 のとき、 f()=x+y
#よって↑をカウントして10^8 * countを後から引けばよい