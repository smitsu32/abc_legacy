#reference: https://drken1215.hatenablog.com/entry/2025/11/16/160322
n,x,y=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

# あまりがすべてのindexで等しいか？
r=a[0]*x%(y-x) # a[i]*x≡a[min]*x mod(y-x)
D=y-x
for i in range(n):
    if a[i]*x%D!=r:
        print(-1)
        exit()

# MX<=P<=mY (m:a[min], M:a[Max],P:合計g)
# mY以下の最大のPを計算し、それがMX以上か？
P=(a[0]*y-r)//D*D+r

if a[-1]*x>P:
    print(-1)
    exit()

ans=0
for i in range(n):
    ans+=(P-a[i]*x)//D

print(ans)