from bisect import bisect_left,bisect_right

n,m=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))

ok,ng=10**10,0
# print(a,b)
while abs(ok-ng)>1:
    mid=(ok+ng)//2
    sell=bisect_right(a,mid)    # 売る人(mid円以下の人数)
    buy=m-bisect_left(b,mid)    # 買う人(mid円以上の人数)
    if sell>=buy:               # 題意を満たすならok下げる
        ok=mid
    else:
        ng=mid
print(ok)