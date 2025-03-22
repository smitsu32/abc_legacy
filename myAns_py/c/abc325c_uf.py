from atcoder.dsu import DSU

h,w=map(int,input().split())
s=[input() for _ in range(h)]

def ne(i,j):        # '#'の隣接マスのリスト
    next=[]
    st=[-1,0,1]
    for di in st:
        for dj in st:
            if not (di==0 and dj==0):
                if 0<=i+di<=h-1 and 0<=j+dj<=w-1:
                    next.append([i+di,j+dj])
    return next

uf=DSU(h*w+1)                   # UnionFind
x=h*w
for i in range(h):
    for j in range(w):
        past=i*w+j             # 一次元化
        
        if s[i][j]=='.':        # '.'ならuf最大のグループにマージ
            uf.merge(past,x)
            continue
        
        for toi,toj in ne(i,j): 
            to=toi*w+toj
            if s[toi][toj]=='#':        # どちらも'#'ならマージ
                uf.merge(past,to)

print(len(uf.groups())-1)       # '.'のグループを引く