from bisect import bisect_right, bisect_left
n=int(input())
s=set()

ans=n

for i in range(n):
    si=input()
    ti=si[::-1]
    if si not in s and ti not in s:     # set()の探索はO(1)
        s.add(si)
        continue
    else:                               # もうあったら棒を減らす
        ans-=1

print(ans)