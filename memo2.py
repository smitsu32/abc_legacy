s=input(); t=input()
t=t.lower()

ans,c,d=0,0,3

if t[2]=='x': d=2

for i in range(d):
    for j in range(c,len(s)):
        if t[i]!=s[j]: continue
        else:
            c=j+1; ans+=1
    if ans==d: break


if ans==3 or (ans==2 and t[2]=='x'): print('Yes')
else: print('No')