from sortedcontainers import SortedList
from bisect import bisect_left,bisect_right

h,w,q=map(int,input().split())
row=[SortedList([i for i in range(w)]) for _ in range(h)]  #横方向にh回
col=[SortedList([i for i in range(h)]) for _ in range(w)]  #縦方向にw回

for _ in range(q):
    r,c=map(int,input().split())
    r-=1; c-=1
    # print(row)
    # print(col)
    
    pos=row[r].bisect_left(c) #爆弾から左方向にみたときの最初の壁のインデックス
    # print(pos)
    
    if pos<len(row[r]) and row[r][pos]==c:  #入力地点に爆弾があるとき
        row[r].discard(c)
        col[c].discard(r)
        continue
    
    if pos<len(row[r]): #範囲内に爆弾があるとき(右)
        posi=row[r][pos]
        row[r].discard(posi)
        col[posi].discard(r)
    if pos>0:           #左
        posi=row[r][pos-1]
        row[r].discard(posi)
        col[posi].discard(r)
    
    
    pos=col[c].bisect_left(r) #爆弾から上方向(転置行列で考える)
    
    # if pos<len(row[c]) and col[c][pos]==r:  #入力地点に爆弾があるとき（重複処理）
    #     col[r].discard(c)
    #     row[c].discard(r)
    #     continue
    # print(pos)
    
    if pos<len(col[c]):     #下
        posi=col[c][pos]
        col[c].discard(posi)
        row[posi].discard(c)
    if pos>0:               #上
        posi=col[c][pos-1]
        col[c].discard(posi)
        row[posi].discard(c)
        
# print(row)
# print(col)
print(sum(len(i) for i in row))