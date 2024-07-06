n,m=map(int,input().split())
s=input()

l=0
usel,usem=0,0
for i in range(n):
    if s[i]=='0':
        usel=0; usem=0
    elif s[i]=='1':
        if usem==m:
            if usel==l:
                l+=1
            usel+=1
        else:
            usem+=1
    else:
        if usel==l:
            l+=1
        usel+=1

print(l)