# ABC310b 上位互換は存在するか？
n,m= map(int,input().split())
p,c,f=[],[],[]
for i in range(n):
    samp=list(map(int,input().split()))
    p.append(samp[0]); c.append(samp[1]); f.append(samp[2:])

# j行がi行の上位互換(jよりiが安いor高機能)ならYes
for i in range(n):
    for j in range(n):
        if (p[i]>p[j] and c[i]<=c[j]) or (p[i]==p[j] and c[i]<c[j]):
            frag=True
            for k in range(c[i]):
                if f[i][k] not in f[j]: frag=False
            if frag: exit(print('Yes'))

print('No')