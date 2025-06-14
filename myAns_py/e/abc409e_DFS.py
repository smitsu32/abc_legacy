n=int(input())
x=list(map(int,input().split()))

e=[[] for _ in range(n)]
for _ in range(n-1):
    u,v,w=map(int,input().split())
    e[u-1].append((v-1,w))
    e[v-1].append((u-1,w))


ans=0
stack=[(0,-1, True)] # (now, parent, go:true/ back:false)

while stack:
    now, parent, go = stack.pop()
    if go:
        stack.append((now, parent, False))  # reserve back (now->parent)
        for v, w in e[now]:
            if v != parent:
                stack.append((v, now, True))  # continue going(now->v)
    else: # elif back
        for v, w in e[now]:
            if v != parent:
                ans += w * abs(x[v]) #重み＊子ノードの絶対値
                x[now] += x[v]

print(ans)