# ABC274 A 割り算の小数第3位まで
#    1 2
# or 3 4

a, b = map(int, input().split())

ans = '{:.3f}'.format(b/a)      ## {インデックス.桁数+f(小数点以下).format(数字)}
print(ans)