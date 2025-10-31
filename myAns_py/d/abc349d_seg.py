## segment tree 
l,r=map(int,input().split())

ans=[]
while l!=r:
    p=1 # power fuctor
    while l%(2*p)==0 and l+(2*p)<=r:
        p*=2
    
    ans.append([l,l+p])
    l+=p

n=len(ans)
print(n)
for i in range(n):
    print(ans[i][0],ans[i][1])