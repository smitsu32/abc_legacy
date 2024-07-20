n=int(input())
a=list(map(int,input().split()))
w=list(map(int,input().split()))

st=[[] for i in range(len(a)+1)]
for i in range(len(a)):
    st[a[i]].append(w[i])
# print(st)
ans=0
for i in range(len(st)):
    if len(st[i])>=2:
        ans+=sum(st[i])-max(st[i])

print(ans)