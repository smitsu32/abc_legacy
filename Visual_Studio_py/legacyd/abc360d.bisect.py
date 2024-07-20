import bisect
# bisect_right(l,x[i]) x[i]はlの何番目に挿入できるか(右側)
# l=[1,2,2,3] x[i]=2 -> 4
n,t=map(int,input().split())
s=input()
x=list(map(int,input().split()))

l,r=[],[]
for i in range(n):
    if s[i]=='0':
        l.append(x[i])
l.sort()

# 2分探索
# 右向きのものが左向きの何番目の右にあるかを調べる
# O(logN)
ans=0
for i in range(n):
    if s[i]=='1':
        af=bisect.bisect_right(l,x[i]+2*t)   # 移動後は左向き(l)の何番目か
        bef=bisect.bisect_right(l,x[i])      # 移動前は左向きの何番目か 
        ans+=af-bef

print(ans)