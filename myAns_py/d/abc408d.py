t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    # C: 0の累積和-1の累積和
    zero,one=0,0
    sumone=0
    C=[0]
    for i in range(n):
        if s[i] == '0':
            zero+=1
        else:
            one+=1
            sumone+=1
        C.append(zero-one)
    
    # min(Cr-Cl)を求める 
    # 範囲外の0を変える(zero[l:r+1])　＋　# 範囲外の1を変える(sum(one)-sum(one[l:r+1]))
    
    nowmax=C[0]
    minc=10**7
    # 尺取りみたいにl.rを動かし、max(C[r]-C[l])を求める
    for i in range(n+1):
        minc=min(minc,C[i]-nowmax)
        nowmax=max(nowmax,C[i])
        
    print(sumone + minc)