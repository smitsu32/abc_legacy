n=int(input())
a=list(map(int,input().split()))

if n==1:
    print(0)
    exit()

ans=0

d=dict()
l=0
for r in range(0,n-1,2):
    if a[r]!=a[r+1]:
        d=dict()
        l=r+2 #forの次のrと同値
    else:
        if a[r] not in d:
            d[a[r]]=r
            ans=max(ans,r-l+1+1) #a[r+1]分をたす
        else:
            l=max(l,d[a[r]]+2) #現在の値or一個前の数字の次に(ex.[2 2 1 1 "1" 1 '2' 2]の'2'ではl=max(l,a[r]+2)=max(4,2)=4)
            d[a[r]]=r           # 重複値だけ上書きすればよい
            ans=max(ans,r-l+1+1)
    # print(d,l,r)

d=dict()
l=1
for r in range(1,n-1,2):
    if a[r]!=a[r+1]:
        d=dict()
        l=r+2
    else:
        if a[r] not in d:
            d[a[r]]=r
            ans=max(ans,r-l+1+1) #a[r+1]分をたす
        else:
            l=max(l,d[a[r]]+2) #現在の値or一個前の数字の次に
            d[a[r]]=r
            ans=max(ans,r-l+1+1)

print(ans)