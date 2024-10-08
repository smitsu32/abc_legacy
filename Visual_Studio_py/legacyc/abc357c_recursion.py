n=int(input())

# 再起関数
def f(n):
    if n==0: return '#'
    
    # レベルn-1を呼び出し
    f1=f(n-1)
    le=len(f1)
    grid=[['.'for _ in range(3*le)]for _ in range(3*le)] #レベルkは(k-1)*3行列
    
    for i in range(3):          # 3つごとにk回くりかえし, k=3 ...(k=0) ...(k=1) ...(k=2)
        for j in range(3):      
            
            if i!=1 or j!=1:    # 余り1(and)だけ無条件で'.'だから除外
                for k in range(le):
                    for l in range(le):
                        grid[le*i+k][le*j+l]=f1[k][l]   # レベルk-1を9回繰り返し写す
                                                        # ただし3*3の真ん中は除く
    return grid

grid=f(n)
for i in grid:
    print(''.join(i))

# レベル1(以下[1]とする)
# ###
# #.#
# ###

# レベル2([2])
# [1][1][1]
# [1] . [1]
# [1][1][1]

# レベル３
# [2][2][2]
# [2] . [2]
# [2][2][2]

# これは下と同じ

# k=len([1])=3 より

#    k=0      k=1      k=2
# i 0  1  2  0  1  2  0  1  2
#j
#0 [1][1][1][1][1][1][1][1][1]
#1 [1] . [1][1] . [1][1] . [1]
#2 [1][1][1][1][1][1][1][1][1]
#0 [1][1][1] .  .  . [1][1][1]
#1 [1] . [1] .  .  . [1] . [1]
#2 [1][1][1] .  .  . [1][1][1]
#0 [1][1][1][1][1][1][1][1][1]
#1 [1] . [1][1] . [1][1] . [1]
#2 [1][1][1][1][1][1][1][1][1]