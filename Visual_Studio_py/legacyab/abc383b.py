h,w,d=map(int,input().split())
s=[input() for i in range(h)]

def eu(i1,j1,i2,j2):
    if abs(i1-i2)+abs(j1-j2)<=d:
        return True
    else:
        return False

ans=0
for i1 in range(h):
    for j1 in range(w):
        if s[i1][j1]=='.':
            for i2 in range(h):
                for j2 in range(w):
                    if s[i2][j2]=='.' and (i1,j1)!=(i2,j2):
                        
                        ansi=0
                        for i in range(h):
                            for j in range(w):
                                if s[i][j]=='.' and (eu(i1,j1,i,j) or eu(i2,j2,i,j)):
                                    ansi+=1
                        ans=max(ans,ansi)

print(ans)