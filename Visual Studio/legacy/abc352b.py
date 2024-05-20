#ABC352B sがtの何文字目か表示する
s = input()
t = input()
i = j = 0

# print(len(s))
for _ in range(len(t)):
    if s[i] == t[j]:
        print(j+1,end=' ')
        j += 1
        i += 1
    else:
        j += 1