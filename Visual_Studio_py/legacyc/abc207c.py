n=int(input())
l,r=[],[]
for i in range(n):
    ti,li,ri=map(int,input().split())
    if ti==1:
        l.append(li)
        r.append(ri)
    elif ti==2:
        l.append(li)
        r.append(ri-0.5)
    elif ti==3:
        l.append(li+0.5)
        r.append(ri)
    else:
        l.append(li+0.5)
        r.append(ri-0.5)

ans=0
for i in range(n-1):
    for j in range(i+1,n):
        if max(l[i],l[j])<=min(r[i],r[j]):
            ans+=1

print(ans)