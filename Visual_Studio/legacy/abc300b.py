#ABC300b グリッド縦横シフト
h,w=map(int,input().split())
a=[list(input())for _ in range(h)]
b=[list(input())for _ in range(h)]

for _ in range(h):
    # aの最後の行を最初に持ってくる(.popは破壊コマンド)
    temp=a.pop()
    a.insert(0,temp)

    for i in range(w):
        for j in range(h):
            # a j行目の最後の列を最初に持ってくる(j:0->h)
            temp=a[j].pop()
            a[j].insert(0,temp)
        if a==b: exit(print('Yes'))

print('No')