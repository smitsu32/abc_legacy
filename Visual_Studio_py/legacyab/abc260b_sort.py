n,x,y,z=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=[]
for i in range(n):
    c.append([a[i],b[i],a[i]+b[i],i+1])

ans=[]
s=set()
c.sort(key=lambda x:x[0],reverse=True)
for i in range(x):
    ans.append(c[i][3])
    s.add(c[i][3])
    # print(c[i][0],c[i][3])

c.sort(key=lambda x:(-x[1],x[3])) # 2段階ソート
now,i=0,0
while now<y:
    if c[i][3] not in s:
        now+=1
        ans.append(c[i][3])
        s.add(c[i][3])
        # print(c[i][1],c[i][3])
    i+=1

c.sort(key=lambda x:(-x[2],x[3]))
# print(c)
now,i=0,0
while now<z: 
    if c[i][3] not in s:
        now+=1
        ans.append(c[i][3])
        s.add(c[i][3])
        # print(c[i][2],c[i][3])
    i+=1

ans.sort()
print(*ans,sep='\n')