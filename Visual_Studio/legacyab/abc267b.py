s=list(input())

for i in range(10):
    s[i]=int(s[i])

if s[0]==1:
    print('No')
    exit()

c=[1 for _ in range(7)]

if s[6]==0:             c[0]=0
if s[3]==0:             c[1]=0
if s[7]==0 and s[1]==0:  c[2]=0
if s[0]==0 and s[4]==0:  c[3]=0
if s[8]==0 and s[2]==0:  c[4]=0
if s[5]==0:             c[5]=0
if s[9]==0:             c[6]=0  # 0 列が全て倒れたとき
# print(s,c)
for i in range(2,7):
    for j in range(i-1):
        
        if c[i]==1 and c[j]==1:
            for k in range(j+1,i):  # 残ってる列の間の列
                if c[k]==0:
                    print('Yes')
                    exit()

print('No')