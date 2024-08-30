_=input()
s=list(input())
q=int(input())

query=[]
lastul=-1
for i in range(q):
    t,x,c=input().split()
    query.append([int(t),int(x)-1,c])
    if t=='2' or t=='3':
        lastul=i                # lower,upperは最後のindexのみ

for i,(t,x,c) in enumerate(query):
    if t==1:
        s[x]=c
    elif t==2 and i==lastul:
        s=list(''.join(s).lower())
    elif t==3 and i==lastul:
        s=list(''.join(s).upper())

print(''.join(s))