n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))

ans=t[:]

# 漸化式　ans[i]=min(ans[i-1]+S[i],t[i])
# 円周を考慮して２周まわす  : end->1->...->end-1
for i in range(2*n):
    ans[i%n]=min(ans[(i-1)%n]+s[(i-1)%n],ans[i%n])

print(*ans,sep='\n')