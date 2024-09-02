n=int(input())
xy=[]
for i in range(n):
    x,y=map(int,input().split())
    xy.append([x,y])
s=input()

r,l=dict(),dict()       # r[y]=min(x), l[y]=max(x) として2変数を管理, inがO(1)

for i in range(n):
    if s[i]=='R':
        if xy[i][1] in l and l[xy[i][1]]>xy[i][0]:
            print('Yes')
            exit()
        elif xy[i][1] in r:
            r[xy[i][1]]=min(r[xy[i][1]],xy[i][0])
        else:
            r[xy[i][1]]=xy[i][0]
    else:
        if xy[i][1] in r and r[xy[i][1]]<xy[i][0]:
            print('Yes')
            exit()
        elif xy[i][1] in l:
            l[xy[i][1]]=max(l[xy[i][1]],xy[i][0])
        else:
            l[xy[i][1]]=xy[i][0]
            
print('No')