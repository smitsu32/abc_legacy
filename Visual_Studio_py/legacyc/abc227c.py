n=int(input())

ans=0
#端数が怖いので余分に
for i in range(1,int(n**(1/3))+10): # 64なら(4,?,?)がimax
    if i**3>n: break
    for j in range(i,int((n/i)**0.5)+10): # 100なら(1,10,?)がjmax
        if i*j**2>n: break
        ans+=n//(i*j)-j+1 #j未満除外

print(ans)