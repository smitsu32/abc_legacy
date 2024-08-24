# from itertools import combinations
k=int(input())
num=['9','8','7','6','5','4','3','2','1','0']       # 大きい順にconbination->bitで数えればよくね？

ans=[]
for bit in range(1<<10):    # 2^10個のbitを生成（）
    s=''
    use=[False]*10          # bit表記で1のときTrue(今回は使わない)
    for i in range(10):      # 0*n-1まで(0,1,2,3)
        if bit & (1<<i):    # nの2進数(bit)と0001->0010->0100->...(i)を比較
            use[i]=True
            s+=num[i]
    if s!='':
        ans.append(int(s))
        
ans=sorted(ans)
print(ans[k]) 