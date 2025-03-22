from bisect import bisect_left,bisect_right

n=int(input())
a=list(map(int,input().split()))
b=sorted(list(set(a)))

ans=[0]*n
for i in range(n):
    ans[len(b)-bisect_right(b,a[i])]+=1 # ans[x] x:a[i]より大きいもの
print(*ans,sep='\n')