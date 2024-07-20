#ABC304 a
from collections import deque

n = int(input())

s = []
a = []

for i in range(n):
    s1,a1 = input().split()
    s.append(s1)
    a.append(int(a1))

# num：a(昇順)にソートしたリスト
num = sorted((range(n)), key=lambda i: a[i])

# sorted_s: sの順番をソートしたリスト
# sorted_s = [s[i] for i in num]
# このままだと小さい順に出力される

first = num[0]

# 時計回りにソート
def clock(l,shift):
    d = deque(l)
    d.rotate(shift)
    return list(d)

ans = clock(s, -1*first)

for i in range(n):
    print(ans[i])