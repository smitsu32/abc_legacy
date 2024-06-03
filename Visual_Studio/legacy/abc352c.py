#ABC352c 巨人の肩に立つ(max(n)=10^5)
n=int(input())
a,b,c=['']*n,['']*n,0
for i in range(n):
    a[i],b[i]=map(int,input().split())
    if b[i]-a[i]>c:
        c=b[i]-a[i]
# print(a,b)

print(sum(a)+c)