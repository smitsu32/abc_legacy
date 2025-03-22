from itertools import permutations

n,s,t=map(int,input().split())

def dist(a,b):
    return (abs(a[0]-b[0])**2+abs(a[1]-b[1])**2)**0.5

ad=[]
ansmin=0
for _ in range(n):
    a,b,c,d=map(int,input().split())
    ad.append([(a,b),(c,d)])
    ansmin+=dist((a,b),(c,d))/t

ans=10**9
for l in permutations(range(n)):
    for bit in range(1<<n):
        v=[0]*n
        for i in range(n):
            if bit&(1<<i):
                v[i]=1
        
        ansi=0
        pos=(0,0)
        for i in range(n):
            if v[l[i]]==0:  # v[l[i]]==0ならpos->(a,b)の距離
                ansi+=dist(ad[l[i]][0],pos)/s
                pos=ad[l[i]][1]
            else:           # pos->(c,d)
                ansi+=dist(ad[l[i]][1],pos)/s
                pos=ad[l[i]][0]
        # print(ansi,l,v)
        ans=min(ans,ansi)

print(ans+ansmin)