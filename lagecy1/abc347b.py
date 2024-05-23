#ABC347 B 文字列内の文字列の種類
s = input()
a = []

# range(a,b+1)はa以上b以下
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        a.append(s[i:j])

# print(a)
print(len(set(a)))