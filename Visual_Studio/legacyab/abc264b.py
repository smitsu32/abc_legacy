r,c=map(int,input().split())

a=max(abs(r-8),abs(c-8))    # 中心からの距離のうち大きい方
if a%2==1:
    print('black')
else:
    print('white')