# ABC322B 接頭接尾語判定
n,m=map(int,input().split())
s=input()
t=input()

ans=0
for i in range(n):
    if s[i]!=t[i]:
        ans+=2; break

ch=n
for i in range(n):
    if s[i]==t[-n+i]:
        ch-=1
if ch!=0: ans+=1

print(ans)