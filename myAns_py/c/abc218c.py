n=int(input())
s=[input() for _ in range(n)]
t=[input() for _ in range(n)]

sc,tc=0,0
for i in range(n):
    for j in range(n):
        if s[i][j]=='#': sc+=1
        if t[i][j]=='#': tc+=1
if sc!=tc: exit(print('No')) #必要

def rot(s):
    return list(zip(*s[::-1]))

def cs(s):
    for i in range(n):
        for j in range(n):
            if s[i][j]=='#':
                return i,j

def check(si,sj,ti,tj):
    offseti=ti-si
    offsetj=tj-sj
    for i in range(n):
        for j in range(n):
            i2=i+offseti
            j2=j+offsetj
            if 0<=i2<n and 0<=j2<n:
                if s[i][j]!=t[i2][j2]:
                    return False
            else:
                if s[i][j]=='#':
                    return False
    return True

for _ in range(4):
    si,sj=cs(s)
    ti,tj=cs(t)
    
    if check(si,sj,ti,tj):
        print('Yes')
        exit()
    
    s=rot(s)
print('No')