n = int(input())
a = list(map(int, input().split()))
s = []
t = []
for _ in range(n-1):
    si,ti = map(int, input().split())
    s.append(si)
    t.append(ti)

# TLE注意
for i in range(n-1):
    if a[i] // s[i] >= 1:
        a[i+1] += (a[i]//s[i]) * t[i]

print(a[-1])