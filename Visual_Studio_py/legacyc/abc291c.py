n=int(input())
s=input()

x,y=0,0
S=set()
S.add((0,0))

for i in range(n):
    if s[i]=='R':
        x+=1
    elif s[i]=='L':
        x-=1
    elif s[i]=='U':
        y+=1
    else:
        y-=1
    
    if (x,y) in S:
        print('Yes')
        exit()
    S.add((x,y))

print('No')