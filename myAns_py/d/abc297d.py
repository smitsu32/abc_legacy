a,b=map(int,input().split())

ans=0
while b!=0:
    ans+=a//b
    a=a%b
    a,b=b,a #a>bにして繰り返す
    # print(a,b,ans)

print(ans-1)