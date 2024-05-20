#ABC334B ax+mを満たすl<x<rの個数は？
a,m,l,r=map(int,input().split())
dl=(l-a)//m
dr=(r-a)//m

# 最小値の余りが0のとき、１個多く消している
ans=dr-dl
if (l-a)%m==0:
    ans+=1

print(ans)