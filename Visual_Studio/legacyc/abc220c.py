n=int(input())
a=list(map(int,input().split()))
x=int(input())

b=sum(a)

ans1=(x//b)*len(a)
x%=b

# 累積和
ans2=0
now=0
for i,ai in enumerate(a): # enumerate （i,リスト[i]）を出力
    now+=ai
    if now>x:
        ans2=i+1
        break

ans=ans1+ans2
print(ans)