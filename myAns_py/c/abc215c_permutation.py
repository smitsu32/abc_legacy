from itertools import permutations

mp=lambda: map(int,input().split())

s,k=input().split()
k=int(k)

p=permutations(s)           # 並び替え列挙 タプルで ('a','a','b')

ans=set()
for i in p:
    ansi=''.join(i)
    ans.add(ansi)

ans=list(ans)
ans.sort()

print(ans[k-1])