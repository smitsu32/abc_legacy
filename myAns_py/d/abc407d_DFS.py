# reference: https://atcoder.jp/contests/abc407/submissions/66137234

import sys
sys.setrecursionlimit(10**6)

h,w=map(int, input().split())

a=[list(map(int, input().split())) for _ in range(h)]
xor_init=0
for i in range(h):
    for j in range(w):
        xor_init^=a[i][j]

visited=[[False]*w for _ in range(h)]
xor=xor_init

def dfs(x,y,nxor):
    global xor
    xor=max(xor,nxor)
    
    # 置かない場所を選ぶ
    for i in range(x,h):
        for j in range(w): # (y,w)ではない
            if x==i and j<y: #現在の行のみ前を見ず、その後は自由 　　　左下を見るため！！！
                continue
            
            if j+1<w and not (visited[i][j] or visited[i][j+1]): # 横
                visited[i][j]=True
                visited[i][j+1]=True
                dfs(i, j+1, nxor^a[i][j]^a[i][j+1]) # XORをとる
                visited[i][j]=False
                visited[i][j+1]=False
            
            if i+1<h and not (visited[i][j] or visited[i+1][j]): # 縦
                visited[i][j]=True
                visited[i+1][j]=True
                dfs(i, j, nxor^a[i][j]^a[i+1][j]) # XORをとる
                visited[i][j]=False
                visited[i+1][j]=False

dfs(0, 0, xor_init)
print(xor)