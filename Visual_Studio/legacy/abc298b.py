# ABC298b グリッド90度回転
import copy
def lmpn(a):
    return [list(map(int,input().split())) for _ in range(a)]

n=int(input())
a=lmpn(n); b=lmpn(n)

for k in range(4):
    temp=[['' for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[i][j]=a[n-1-j][i]
    
    # '=',[:]より便利(非参照)
    a=copy.deepcopy(temp)
    
    frag=True
    for i in range(n):
        for j in range(n):
            if a[j][i]==1:
                if b[j][i]!=1: frag=False
    
    if frag: exit(print('Yes'))

print('No')