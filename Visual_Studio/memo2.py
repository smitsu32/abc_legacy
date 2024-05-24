h,w=map(int,input().split())
a=[list(input())for _ in range(h)]
b=[list(input())for _ in range(h)]

for s in range(h-1):
    c1=a[-1]
    c2=a[:h]
    c=c1+c2
    
    for t in range(w-1):
        d1=a[]