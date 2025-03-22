from itertools import combinations

h1,w1=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h1)]
h2,w2=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(h2)]

for i in list(combinations(range(h1),h2)):  #任意の行,列を選択
    for j in list(combinations(range(w1),w2)):
        flag=True
        for k in range(h2):
            for l in range(w2):
                if a[i[k]][j[l]]!=b[k][l]:  #全て等しいときTrue
                    flag=False
        if flag:
            print('Yes')
            exit()
print('No')