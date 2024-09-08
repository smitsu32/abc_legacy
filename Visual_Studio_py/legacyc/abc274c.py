n=int(input())
a=list(map(int,input().split()))

ans=[0]*(2*n+1)
for i in range(n):
    ans[2*i+1]=ans[a[i]-1]+1    # aは１始まり,ansは0始まり
    ans[2*i+2]=ans[a[i]-1]+1

print(*ans,sep='\n')