n=int(input())
s=input()

pos=[]
for i in range(n):
    if s[i]=='1':
        pos.append(i)

c=(max(pos)+min(pos))//2

le=len(pos)

ans=0
if le%2==1:
    m=pos[le//2] #meanの左端
    m-=le//2
    for i in range(le):
        ans+=abs(m+i-pos[i])
else:
    ans1,ans2=0,0
    m1=pos[le//2] #meanの左端
    m1-=le//2
    m2=m1+1
    for i in range(le):
        ans1+=abs(m1+i-pos[i])
        ans2+=abs(m2+i-pos[i])
    ans=min(ans1,ans2)
    
print(ans)