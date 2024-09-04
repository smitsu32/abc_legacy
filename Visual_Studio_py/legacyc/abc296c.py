n,x=map(int,input().split())
a=set(list(map(int,input().split())))
b=sorted(a) # list

for i in range(len(a)):
    if b[i]+x in a or b[i]-x in a:
        print('Yes')
        exit()
print('No')