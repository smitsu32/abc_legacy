a=[list(map(int,input().split())) for _ in range(9)]

flag=True
for i in range(9):
    s1,s2=[],[]
    for j in range(9):
        if a[j][i] in s1 or a[i][j] in s2:
            flag=False
        s1.append(a[j][i])
        s2.append(a[i][j])

for i in range(3):
    for j in range(3):
        s=[]
        for k in range(3):
            for l in range(3):
                if a[3*j+l][3*i+k] in s:
                    flag=False
                s.append(a[3*j+l][3*i+k])

if flag:
    print('Yes')
else:
    print('No')