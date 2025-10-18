l=[] # (()のバランス, 左の最小値)

for _ in range(int(input())):
    que=input().split()
    if que[0]=='1':
        if que[1]=='(':
            if len(l)>0:
                lb,mn=l[-1]
                b=lb+1
                if mn>b: mn=b
            else:
                b,mn=1,1
            l.append((b,mn))
        else:
            if len(l)>0:
                lb,mn=l[-1]
                b=lb-1
                if mn>b: mn=b
            else:
                b,mn=-1,-1
            l.append((b,mn))
    else:
        l.pop()
    
    if len(l)>0:
        b,mn=l[-1]
    else:
        b,mn=0,0
        
    if b==0 and mn>=0:
        print('Yes')
    else:
        print('No')