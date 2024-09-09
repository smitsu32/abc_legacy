n=int(input())
p=list(map(int,input().split()))
pl=[0]*n    # i回動かして喜ぶ人数pl[i]

for i in range(n):
    pl[(i-p[i])%n]+=1   # 人iは初期位置p[i]からiまで動くと正面に来る
    pl[(i-p[i]-1)%n]+=1
    pl[(i-p[i]+1)%n]+=1

ans=0
for i in pl:
    ans=max(ans,i)
print(ans)