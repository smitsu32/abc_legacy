n=int(input())
a=sorted(list(map(int,input().split())))
mean=sum(a)//n
ans1,ans2=0,0
for i in range(n):
    if a[i]<mean:       # 小さいのを(平均)-0.x にもっていく
        ans1+=mean-a[i]
    elif a[i]>mean:
        ans2+=a[i]-(mean+1) # 大きいのを(平均)+0.x にもっていく

print(max(ans1,ans2))   # 上のどちらも充足する必要があるためmax