from collections import defaultdict,deque

h,w,n=map(int,input().split())

H,W=defaultdict(deque),defaultdict(deque)
p=[]

for i in range(n):
    hi,wi=map(int,input().split())
    H[hi].append(i)
    W[wi].append(i)
    p.append((hi,wi))

# たてHのものを処理 → 現在のy座標をすすめ、Wを短縮
# ↓
# よこWのものを処理 → 現在のx座標をすすめ、Hを短縮し、くりかえし
ans=[None]*n
used=[False]*n
nowx,nowy=1,1 # w,h

for _ in range(n-1):
    while H[h]:
        tmp=H[h].popleft() #index
        if used[tmp]:
            continue
        
        ans[tmp]=(nowx,nowy)
        used[tmp]=True
        
        nowy+=p[tmp][1] # 座標をyすすめる
        w-=p[tmp][1]
        
        break
    
    else:
        while W[w]:
            tmp=W[w].popleft()
            if used[tmp]:
                continue
            
            ans[tmp]=(nowx,nowy)
            used[tmp]=True
            
            nowx+=p[tmp][0] # 座標をyすすめる
            h-=p[tmp][0]
            
            break

# None防止用
for i in range(n):
    if not used[i]:
        ans[i]=(nowx,nowy)

for i in ans:
    print(*i)