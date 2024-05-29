h,w=map(int,input().split())

s=[list(input()) for _ in range(h)]

hc,wc,he,we=0,0,0.0
frag1=True
for i in range(w):
    for j in range(h):
        if s[j][i]=='#' and frag1:
            hc,he=j,j; wc,we=i,i; frag1=False
        elif s[j][i]=='#' and (wc!=we or hc!=)