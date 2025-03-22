from heapq import heapify,heappop,heappush

H,w,x=map(int,input().split())
p,q=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(H)]
p-=1; q-=1

def next(i,j):
    global h,seen,ans
    for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
        ni,nj=i+di,j+dj
        if 0<=ni<H and 0<=nj<w and (ni,nj) not in seen:
            heappush(h,(s[ni][nj],ni,nj))
            # if s[ni][nj]<ans/x:
            #     ans+=s[ni][nj]
            #     seen.add((ni,nj))

seen=set()
seen.add((p,q))
h=[]
heapify(h)
next(p,q)
ans=s[p][q]
while h:
    k,i,j=heappop(h)
    # print((i,j),ans,seen)
    if (i,j) in seen:
        continue
    seen.add((i,j))
    
    if s[i][j]<ans/x:
        ans+=s[i][j]
        next(i,j)

print(ans)