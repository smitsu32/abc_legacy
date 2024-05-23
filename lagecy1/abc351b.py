#ABC351 B n*n次元配列入力
n = int(input())

# リスト内包形式をマスターしたい
a = [input() for _ in range(n)]
b = [input() for _ in range(n)]

[print(i+1, j+1) for i in range(n) for j in range(n) if not a[i][j] == b[i][j]]
