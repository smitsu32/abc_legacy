#ABC350B 偶奇における分岐処理
n,q = map(int, input().split())

## 入力が複数行のとき
## t = [int(input()) for _ in range(q)]
# 入力が１行にまとまってるとき
t = list(map(int, input().split()))

ans = n

# 歯1本ずつ偶奇判定、奇数回なら1本減少
for i in range(n):
    if t.count(i+1) % 2 == 1:
        ans -= 1

print(ans)