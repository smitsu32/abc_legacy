k,g,m=map(int,input().split())
gnow,mnow=0,0

for _ in range(k):
    if gnow==g:
        gnow=0
    elif mnow==0:
        mnow=m
    else:
        if mnow>=g-gnow:
            mnow-=g-gnow; gnow=g
        else:
            gnow+=mnow; mnow=0

print(gnow,mnow)