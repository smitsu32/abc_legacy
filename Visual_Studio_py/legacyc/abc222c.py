n,m=map(int,input().split())
a=[input() for _ in range(2*n)]

# [i,j]: 勝ち数iのjさん
ans=[[0,j] for j in range(2*n)]

for i in range(m):
    for j in range(n):
        p1,p2=ans[2*j][1],ans[2*j+1][1]
        c1,c2=a[p1][i],a[p2][i]
        if (c1,c2)==('P','G') or (c1,c2)==('C','P') or (c1,c2)==('G','C'):
            ans[2*j][0]+=1
        elif c1==c2: # aiko
            None
        else: #make
            ans[2*j+1][0]+=1
        # print((p1,c1),(p2,c2))
    ans.sort(key=lambda x: (-x[0],x[1]))

for ansi in ans:
    print(ansi[1]+1)