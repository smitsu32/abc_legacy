# ABC289b レ
n,m=map(int,input().split())
a=list(map(int,input().split()))

b=[]; stack=[]
for i in range(n):
    if i+1 in a: stack.append(i+1); continue
    else:
        b.append(i+1)
        if len(stack)!=0:
            stack.reverse()
        b+=stack
        stack=[]

print(*b)