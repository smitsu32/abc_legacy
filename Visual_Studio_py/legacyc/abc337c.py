n=int(input())
a=list(map(int,input().split()))
b=[-1]*n
ans=[]

for i in range(n):             # i人目が何人目の後ろかをbに格納
    if a[i]==-1:
        ans.append(i+1)
    else:
        b[a[i]-1]=i+1

for i in range(n-1):            # 1人目(ans[0])からbをたどる
    ans.append(b[ans[-1]-1])

print(*ans)