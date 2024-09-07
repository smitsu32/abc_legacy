n,k=map(int,input().split())
a=list(map(int,input().split()))
a=set(a)

for i in range(k):  # listだと多分TLE
    if i not in a:
        print(i)
        exit()
print(k)