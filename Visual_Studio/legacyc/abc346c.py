n,k=map(int,input().split())
a=map(int,input().split())
a=sorted(list(set(a)))

l=len(a)
ans=(1+k)*k//2


for i in range(l):
    if a[i]<=k:         # 合計からa[i]を引く
        ans-=a[i]
    
    if i>=k-1: break    # kを過ぎたらbreak

print(ans)