n,q=map(int,input().split())
s=input()
l,r=[],[]
for _ in range(q):
    li,ri=map(int,input().split())
    l.append(li); r.append(ri)

b=[0]           # 隣と比較するのでb[0]=1
a=0
# 累積和
for i in range(1,n):
    if s[i-1]==s[i]:    # ２文字連続なら a+=1
        a+=1
    b.append(a)

# print(b)

for i in range(q):
    ans=b[r[i]-1]-b[l[i]-1]     # (r文字目までの合計)-(l文字目)
    print(ans)