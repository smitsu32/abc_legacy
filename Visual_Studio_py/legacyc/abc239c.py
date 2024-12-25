x1,y1,x2,y2=map(int,input().split())

def eu(x1,y1,x2,y2):
    return (abs(x2-x1)**2+abs(y2-y1)**2)**0.5

s1,s2=set(),set()
for dx,dy in [[1,2],[2,1],[-1,2],[2,-1],[-1,-2],[-2,-1],[-2,1],[1,-2]]:
    s1.add((x1+dx,y1+dy))
    s2.add((x2+dx,y2+dy))

for x,y in s1:
    if (x,y) in s2:
        print('Yes')
        exit()
# print(s1,s2)
print('No')