s,t=input(),input()

def c(s): #ランレングス符号化
    a=[]
    nowi,now=s[0],0
    for i in s:
        if i==nowi:
            now+=1
        else:
            a.append([nowi,now])
            nowi,now=i,1
    if now>=1:
        a.append([nowi,now])
    return a

s,t=c(s),c(t)   # [[a,1],[c,3],... ]

if len(s)!=len(t):
    print('No')
    exit()

for i in range(len(s)):
    if s[i][0]==t[i][0]:
        if s[i][1]==t[i][1] or (s[i][1]>=2 and s[i][1]<t[i][1]):
            continue
    print('No')
    exit()

print('Yes')