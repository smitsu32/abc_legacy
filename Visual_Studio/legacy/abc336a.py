# ABC336 A
n = int(input())
s = input()
num = len(s)

for i in range(num):
    for j in range(i+1, num):
        if s[i] == '|' and s[j] == '|':
            start = i
            end = j
            break

for i in range(num):
    if s[i] == '*':
        p = i

if start < p and p < end:
    print("in")
else:
    print("out")

# print(start, end, p)