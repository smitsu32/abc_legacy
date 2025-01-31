h,w=map(int,input().split())
s=[input() for _ in range(h)]

i1,i2,j1,j2=1e5,-1,1e5,-1
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            i1=min(i1,i)
            i2=max(i2,i)
            j1=min(j1,j)
            j2=max(j2,j)
# print(i1,j1,i2,j2)
for i in range(i1,i2+1):
    for j in range(j1,j2+1):
        if s[i][j]=='.':
            print('No')
            exit()

print('Yes')
