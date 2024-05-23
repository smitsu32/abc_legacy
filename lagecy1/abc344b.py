# ABC344 B 入力数が不定のとき
a = []

while True:
    ai = input()
    a.append(ai)
    if ai == '0':
        break

a.reverse()

for i in range(len(a)):
    print(a[i])