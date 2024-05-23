# ABC319B iがn/jの約数
n=int(input())

#n=12のとき、i:0~12, j:1~9(const)
for i in range(n+1):
    if i==0: print('1', end=''); continue
    for j in range(1,10):
        if n%j==0 and i%(n//j)==0 : print(str(j), end=''); break
        if j==9: print('-', end='')