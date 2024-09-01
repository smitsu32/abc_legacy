from collections import defaultdict

s=list(input())
t=list(input())
al=set(('a','t','c','o','d','e','r','@'))

flag=True

sd=defaultdict(int)
td=defaultdict(int)

for i in range(len(s)):
    if s[i] in al:
        sd[s[i]]+=1
    if t[i] in al:
        td[t[i]]+=1

for i in al:
    if al=='@': continue
    else:
        dif=sd[i]-td[i]
        if dif>=0:
            td['@']-=dif
            sd[i]-=dif
        else:
            sd['@']-=-dif
            td[i]-=-dif
        
        if sd['@']<0 or td['@']<0:
            print('No')
            exit()

if sd==td:
    print('Yes')
else:
    print('No')