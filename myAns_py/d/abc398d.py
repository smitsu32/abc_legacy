n,r,c=map(int,input().split())
s=input()

smoke=set()
fr,fc=0,0 #焚火の座標
smoke.add((fr,fc))
ans=[]
# if (r,c) in smoke:
#     ans.append(1)
# else:
#     ans.append(0)

for i in s:
    if i=='N': #煙を動かしたくない　→　人と焚火を逆向きに動かす！
        fr+=1
        r+=1
    elif i=='S':
        fr-=1
        r-=1
    elif i=='E':
        fc-=1
        c-=1
    else:
        fc+=1
        c+=1
    smoke.add((fr,fc))
    
    if (r,c) in smoke:
        ans.append(1)
    else:
        ans.append(0)

print(*ans,sep='')