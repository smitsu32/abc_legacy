n,m=map(int,input().split())

inc=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    inc[(a+b)%n]+=1

ans=m*(m-1)//2 # 理想の総交差数 線はm-1本なので (1+(m-1)) * (m-1) // 2
for i in range(n):
    ans-=inc[i]*(inc[i]-1)//2 # 平行線同士の交差数を引く

print(ans)