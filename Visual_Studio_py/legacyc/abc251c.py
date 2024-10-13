n=int(input())
a=[]
b=set()
for i in range(n):
    s,t=input().split()
    if s not in b:
        b.add(s)
        a.append([s,int(t),i+1])
a.sort(key=lambda x: x[1],reverse=True)
print(a[0][2])