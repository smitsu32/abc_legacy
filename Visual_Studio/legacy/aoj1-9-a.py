ips=lambda: input().split()
ip=lambda: input()
ii=lambda: int(input())
mp=lambda: map(int,input().split())
lmp=lambda: list(map(int,input().split()))

w=input()
e='END_OF_TEXT'

ans=0
while True:
    si=input()
    if si=='END_OF_TEXT': break
    
    si=si.lower().split()
    ans+=si.count(w)

print(ans)