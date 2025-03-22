n=int(input())
s=input()

ans=1
T=[]
for i in range(1,n-1):
    if s[i]=='/' and s[i-1]=='1' and s[i+1]=='2':
        T.append(i)

for t in T:
    ansi=1
    for i in range(1,n): #1,n//2+1とすること
        if 0<=t-i and t+i<n and s[t-i]=='1' and s[t+i]=='2':
            ansi+=2
        else:
            break
    ans=max(ansi,ans)
print(ans)