n,m=map(int,input().split())

L=[1]*(m+1) #右端固定で左端を探す
for i in range(n):
    l,r=map(int,input().split())
    L[r]=max(L[r],l+1)  # l~rとならない範囲のL[r]~r

for r in range(1,m+1):  # 1-indexed
    L[r]=max(L[r],L[r-1]) #制約より大きい範囲を省く
# print(L) #L[r]: 右端rのとき条件を満たす左端の最小値

ans=0
for r in range(1,m+1):
    ans+=r-L[r]+1       # r-l+1

print(ans)