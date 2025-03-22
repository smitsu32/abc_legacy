from bisect import bisect_left,bisect_right

n,s=int(input()),list(input())
w=list(map(int,input().split()))

c,a=[],[]
for i in range(n):
    if s[i]=='0':
        c.append(w[i])
    else:
        a.append(w[i])

c.sort()
a.sort()

ans=0
for ii in w:
    for j in [-1,1]:
        i=ii+0.1*j  # wの値の前後で最大値を探す
        ch=bisect_left(c,i)
        ad=len(a)-bisect_left(a,i)
        ans=max(ans,ch+ad)
        # print(i,ch,ad)
print(ans)