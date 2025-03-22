# ABC293b 計算量スレスレ
n=int(input())
x=list(map(int,input().split()))

# ifやboolで計算量を減らす
# 代入、演算が遅いため
y=[False]*n; z=[]
for i in range(n):
    if y[i]==False and y[x[i]-1]==False:
        y[x[i]-1]=True

for i in range(n):
    if y[i]==False:
        z.append(i+1)

print(len(z)); print(*z)