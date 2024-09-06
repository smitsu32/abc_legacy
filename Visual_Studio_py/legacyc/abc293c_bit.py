h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]

ans=0
for bit in range(1<<(h+w-2)):
    r=[False]*(h+w-2)   # 移動回数h-1+w-1
    c=0
    
    for i in range(h+w-2):
        if bit&(1<<i):
            r[i]=True
            c+=1
    
    if c!=h-1:
        continue
    
    x,y=0,0
    s=set()
    s.add(a[0][0])
    flag=True
    
    for i in range(h+w-2):
        if r[i]:
            y+=1
        else:
            x+=1
        
        if a[y][x] not in s:
            s.add(a[y][x])
        else:
            flag=False
            break
    if flag:
        ans+=1
    else:
        continue

print(ans)