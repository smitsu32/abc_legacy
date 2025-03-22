def era(n):
    isprime = [True] * n
    res = []
    isprime[0] = False
    isprime[1] = False
    for i in range(2, n):
        if isprime[i]:
            res.append(i)
            for j in range(i * 2, n, i):
                isprime[j] = False
    return res

n=int(input())
# p^8=n or p^2q^2=nなので、高々sqrt(sqrt((4*10**12))=sqrt(2)*10**3まででよい
# 約数の数：n=36 (=2^2*3^2) のとき (2+1)*(2+1)=9個

res=era(2*10**6+1) #かなり尤度をもたせている
ans=0
for i in range(len(res)):
    p=res[i]
    if p**4>n: #p^2*q^2=<n(p<q)を求めるため
        break
    
    if p**8<=n:
        ans+=1
    for j in range(i+1,len(res)):
        q=res[j]
        if p>=q:
            continue
        
        if p**2*q**2<=n:
            ans+=1
        if p**2*q**2>=n:
            break

print(ans)