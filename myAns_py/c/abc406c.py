n=int(input())
p=list(map(int,input().split()))

r=[]
now=0
# ランレングス圧縮
for i in range(n-1):
    if i==0:
        now+=1
        if p[i]<p[i+1]:
            nows='<'
        else:
            nows='>'
    
    else:
        if p[i]<p[i+1]:
            if nows=='<':
                now+=1
            else:
                r.append((nows,now))
                now=1
                nows='<'
        else:
            if nows=='>':
                now+=1
            else:
                r.append((nows,now))
                now=1
                nows='>'
r.append((nows,now))

# << > <<<　の > に注目 = a*b
ans=0
for i in range(1,len(r)-1):
    if r[i][0]=='>':
        ans+=r[i-1][1]*r[i+1][1]

print(ans)