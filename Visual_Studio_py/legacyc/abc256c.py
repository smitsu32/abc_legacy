from itertools import combinations

hw=list(map(int,input().split()))
h,w=hw[:3],hw[3:]

ans=0
for i in range(1,min(w[0],h[0])-1):
    for j in range(1,min(h[0],w[1])-1):
        for k in range(1,min(w[0],h[1])-1):
            for l in range(1,min(w[1],h[1])-1):
                m=h[0]-i-j
                n=h[1]-k-l
                o=w[0]-i-k
                p=w[1]-j-l
                q=w[2]-m-n
                if q==h[2]-o-p: #qの縦横が等しい
                    if m>0 and n>0 and o>0 and p>0 and q>0: #全て正
                        ans+=1
print(ans)

# i j m 
# k l n
# o p q