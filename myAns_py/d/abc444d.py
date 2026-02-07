n=int(input())
a=list(map(int,input().split()))

c=[0]*(max(a)+1)
for i in range(n):
    c[a[i]-1]+=1

now=0
for i in range(len(c)-1,-1,-1):
    c[i]+=now
    now=c[i]
# print(c)
up=0
for i in range(len(c)):
    c[i]+=up
    up=c[i]//10
    c[i]%=10
# print(c)
while up>0:
    c.append(up%10)
    up//=10

print(int(''.join(map(str,c[::-1]))))