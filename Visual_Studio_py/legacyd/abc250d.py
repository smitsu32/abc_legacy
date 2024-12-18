from bisect import bisect_left,bisect_right

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

res=era(10**6)
# resthree=[]
# for i in range(len(res)):
#     resthree.append(res[i]**3)

n=int(input())

ans=0
for i in range(len(res)):
    m=res[i]
    if n//m<8: break
    
    for j in range(i+1,len(res)):
        if n>=m*res[j]**3:
            ans+=1
        else: break
    
print(ans)