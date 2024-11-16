n,k=map(int,input().split())
s=input()
t=[]
for i in range(1,n): #切り替わり後のインデックスを記録
    if s[i-1]!=s[i]:
        t.append(i)
t=[0]+t+[n]
u=[]
for i in range(len(t)-1):
    u.append(s[t[i]:t[i+1]])

one=0
for i in range(len(u)):
    if u[i][0]=='1':
        one+=1
        if one==k:
            u[i],u[i-1]=u[i-1],u[i] #直前の０群と入れ替え
            break

for i in u:
    print(''.join(i),end='')