n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
b.append(a[-1])

ans=a[-1]
for i in range(n-1):
    # print(i)
    if a[i]>b[i]:
        b.insert(i,a[i])
        ans=a[i]
        break

for i in range(n):
    if a[i]>b[i]:
        print(-1)
        exit()
print(ans)