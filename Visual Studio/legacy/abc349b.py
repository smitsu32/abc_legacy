#ABC349B 文字の個数が同じものをカウント
s = input()
ans = []

for i in range(26):
    n = s.count(chr(97+i))
    ans.append(n)

# print(ans)
maxans = max(ans)
# print(maxans)

#range(a,b)はa以上b未満
for i in range(1, maxans+1):
    m = ans.count(i)
    # print(m)
    if m != 0 and m != 2:
        print("No")
        exit()

print("Yes")