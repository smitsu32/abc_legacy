s=list(input())
n=len(s)

ran=[]
num,now=s[0],0
for i in range(n):
    if num==s[i]:
        now+=1
    else:
        ran.append([int(num),now])
        num,now=s[i],1
ran.append([int(num),now])

m=len(ran)
ans=0
for i in range(m-1):
    if ran[i][0]+1==ran[i+1][0]:
        ans+=min(ran[i][1],ran[i+1][1])

print(ans)