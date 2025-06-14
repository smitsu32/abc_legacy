n,m=map(int,input().split())

# lからrの処理がm回ある　→　O(NM)は無理
# imos法
# 始点：c[l]に+1, 終点の次：c[r+1]に-1する
c=[0]*(n+1)
for _ in range(m):
    l,r=map(int,input().split())
    l-=1; r-=1
    c[l]+=1
    c[r+1]-=1

for i in range(1,n+1):
    c[i]+=c[i-1]

print(min(c[:-1])) #最後は番兵なので除外