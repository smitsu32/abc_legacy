# ABC343 B 行列の有要素インデックスを出力
n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 1:
            print(j+1, end = ' ')
    print()
