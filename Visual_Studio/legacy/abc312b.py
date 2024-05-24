# ABC312B Takcode
## ゴリ押し
def tak(ss,x,y):
    for k in range(3):
        for l in range(3):
            if ss[x+k][y+l]!='#' or ss[x+k+6][y+l+6]!='#': return False
    
    for k in range(4):
        if ss[x+3][y+k]!='.' or ss[x+k][y+3]!='.': return False
        elif ss[x+5][y+5+k]!='.' or ss[x+5+k][y+5]!='.': return False
    return True

n,m=map(int,input().split())
s=[input() for _ in range(n)]

for i in range(n-8):
    for j in range(m-8):
        ans=tak(s,i,j)
        if ans==True: print(i+1,j+1)