r,c=map(int,input().split())

# 中心からの距離が大きい所は島縞模様になっている
# 逆に、小さければ全て白or黒になっているため判断しなくていい
m=max(abs(8-r),abs(8-c))

if m%2==0:
    print('white')
else:
    print('black')