n,d=map(int,input().split())
a=list(map(int,input().split()))

cnt=[0]*(10**6+1)
for i in a:
    cnt[i]+=1

if d==0: # d=0のときは、cnt[i]>=2を減らす
    ans=0
    for i in range(len(cnt)):
        ans+=max(cnt[i]-1,0)
    print(ans)
    exit()

def calc(x):
    x=[0]+x # dpとidxを合わせるため
    dp=[0]*(len(x)+1)
    for j in range(1,len(x)): # dp[i] = i番目までに数字を削る最小数
        dp[j+1]=min(dp[j]+x[j], dp[j-1]+x[j-1])
    return dp[-1]

ans=0

# 余りごとにみる -> i,i+d, i+2d, ... から連続しているものを取り除く = DP
for i in range(d):
    cnti=cnt[i::d] # i, i+d, i+2d, ... の数字の個数    
    if not cnti:
        continue # cntiが空ならスキップ
    else:
        ans+=calc(cnti)

print(ans)