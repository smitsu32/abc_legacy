from collections import Counter

n=int(input())
t=Counter()
ans=[]

for i in range(n):
    si=input()
    t.update(si.split())        # 文字列でCounterを作れる
    
    if t[si]<=1:
        ans.append(si)
    else:
        ans.append(si+'('+str(t[si]-1)+')')

print(*ans)