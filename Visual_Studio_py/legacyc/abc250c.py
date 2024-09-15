from copy import deepcopy

n,q=map(int,input().split())
pos,ans=[],[]
for i in range(n):
    pos.append(i)   # iの場所を管理
    ans.append(i)

for _ in range(q):
    i=int(input())-1
    p=pos[i]
    if p==n-1:
        pp=pos[i]-1
    else:
        pp=pos[i]+1
        
    ans[p],ans[pp]=ans[pp],ans[p]   #数字入れ替え
    pos[i],pos[ans[p]]=pos[ans[p]],pos[i]   # 位置入れ替え(ans[p]が変更後)

for i in ans:
    print(i+1,end=' ')