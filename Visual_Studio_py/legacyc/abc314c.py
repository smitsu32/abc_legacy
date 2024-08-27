n,m=map(int,input().split())
s=input()
c=list(map(int,input().split()))

a=[[]for _ in range(m)]     # グループごとにcを整理
for i in range(n):
    c[i]-=1
    a[c[i]].append(i)
# print(a,c)

t=[0]*m     # cの登場回数カウント

ans=''
for i in range(n):
    ans+=s[a[c[i]][t[c[i]]-1]]      # c[i]番目の番号のt[c[i]]-1（1文字ずらし）の文字を出力
    t[c[i]]+=1
# print(t)

print(ans)