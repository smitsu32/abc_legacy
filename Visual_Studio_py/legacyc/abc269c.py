n=int(input())
m=bin(n)[2:]
m=m[::-1]   # 逆順で足していく

ans=[""]

for i in range(len(m)):
    now=[]
    if m[i]=='1':
        for j in ans:
            now.append("1"+str(j))
            now.append("0"+str(j))
    else:
        for j in ans:
            now.append("0"+str(j))
    ans=now # 更新
ans.sort()

for i in ans:
    print(int(i,2)) # binの逆