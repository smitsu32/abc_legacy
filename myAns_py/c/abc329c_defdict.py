from collections import defaultdict
n=int(input())
s=input()

ans=defaultdict(int)
now=0
for i in range(n):
    if i==0:
        ans[s[0]]=1         # sが１文字のとき用
        now+=1
        continue
    
    if s[i-1]==s[i]:
        now+=1
    else:
        now=1                   # 文字が違うとき初期化
        
    ans[s[i]]=max(ans[s[i]],now)    # 今の長さ(ans[s[i]])と連続文字数(now)のmax

print(sum(ans.values()))