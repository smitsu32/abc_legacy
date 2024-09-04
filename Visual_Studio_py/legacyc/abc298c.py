n=int(input())
q=int(input())
m=2*10**5+1
b=[[] for _ in range(n+1)] # ボックスに入っているカード
c=[set() for _ in range(m+1)] # カードが入っているボックス

for _ in range(q):
    qi=list(map(int,input().split()))
    if qi[0]==1:
        i,j=qi[1],qi[2]
        b[j].append(i)
        c[i].add(j)
    elif qi[0]==2:
        i=qi[1]
        bi=sorted(b[i])
        print(*bi)
    else:
        i=qi[1]
        ci=sorted(c[i]) # setは順番が保証されないため
        print(*ci)
