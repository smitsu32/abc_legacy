# ABC342 B 順番が先行している人を出力
def mp() : return map(int, input().split())

n = int(input())
p = list(mp())
q = int(input())
a = []
b = []
for _ in range(q):
    ai,bi = mp()
    a.append(ai)
    b.append(bi)
# 
# print(a,b,p)

for i in range(q):
    for j in range(len(p)):
        if a[i] == p[j]:
            one = j
        elif b[i] == p[j]:
            two = j
    
    if one > two:
        print(b[i])
    else:
        print(a[i])