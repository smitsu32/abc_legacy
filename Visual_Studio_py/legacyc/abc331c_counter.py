from collections import Counter

n=int(input())
a=list(map(int,input().split()))

c=Counter(a)
c=sorted(c.items(), key=lambda x: x[0], reverse=True)   # Counter ((4,2) (2,1) (4,2))

s=0
ans={}          # dict型{2:10 1:8}
for i,j in c:   # i:要素　ｊ:合計
    ans[i]=s
    s+=i*j

for i in a:
    print(ans[i], end=' ')