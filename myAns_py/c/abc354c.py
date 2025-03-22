n=int(input())
ac=[]
for i in range(n):
    aci=list(map(int,input().split()))
    aci.append(i+1)
    ac.append(aci)
ac.sort(key=lambda i: i[1])

ans=[]
maxa=-1
for i in range(n):        
    if ac[i][0]>maxa:   # i-1ではなく 強さ最大のやつと比べる
        ans.append(ac[i][2])
    
    maxa=max(maxa,ac[i][0])

ans.sort()
print(len(ans))
print(*ans)