# ABC340 B クエリ基礎
q = int(input())
query = []
ans = []
for i in range(q):
    qu1, qu2 = map(int,input().split())
    if qu1 == 1:
        query.append(qu2)
    else:
        ans.append(query[-qu2])

print(*ans, sep='\n')