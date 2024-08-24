# defaultdictでスコアの個数を管理
from collections import defaultdict
n,t=map(int,input().split())

s=[0]*n
c=defaultdict(int)      # 0で辞書を初期化
c[0]=n                  # 0は最初nこ
ans=1                   # 種類数(0の１種類)

for i in range(t):
    a,b=map(int,input().split())
    a-=1
    c[s[a]]-=1          # 古いスコアs[a]のカウントを-1する
    if c[s[a]]==0:      # 古いスコアが０個になったら種類-1
        ans-=1
    
    s[a]+=b             # s[a]を更新
    if c[s[a]]==0:      # 新しいスコアが０個なら+1
        ans+=1
    c[s[a]]+=1          # 新しいスコアのカウント+1
    
    print(ans)