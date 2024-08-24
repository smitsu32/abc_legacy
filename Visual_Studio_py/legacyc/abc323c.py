n,m=map(int,input().split())
a=list(map(int,input().split()))

ans,s=[],[]
for i in range(n):
    si=list(input())
    s.append(si)
    ansi=0
    for j in range(len(si)):
        if s[i][j]=='o':
            ansi+=a[j]
    ans.append(ansi+i+1)

ma=max(ans)

for i in range(n):
    b=[]
    for j in range(m):
        b.append([a[j],s[i][j]])
    b=sorted(b, key=lambda x: x[0], reverse=True)

    c=0
    ansi=ans[i]
    
    if ansi==ma:
        print(0)
        continue
    
    flag=False
    while True:
        for j in range(m):
            if b[j][1]=='x':
                if ansi+b[j][0]>ma:
                    c+=1
                    flag=True
                    break
                else:
                    ansi+=b[j][0]
                    c+=1
        if flag:
            print(c)
            break
