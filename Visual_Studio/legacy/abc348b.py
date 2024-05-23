# ABC348 B 各点から最長距離の点を出力
import math
def mp() : return map(int,input().split())

n = int(input())
x = []
y = []

for _ in range(n):
    xi,yi = mp()
    x.append(xi)
    y.append(yi)

for i in range(n):
    dismax = 0
    ans = 1
    for j in range(n):
        dis = math.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
        if dis > dismax:
            dismax = dis
            ans = j + 1
    print(ans)