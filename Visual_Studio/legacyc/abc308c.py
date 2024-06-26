from decimal import Decimal     # 浮動小数点の精度が上がる(Cpythonで提出)
n=int(input())
s=[]

for i in range(n):
    ai,bi=map(int,input().split())
    ai=Decimal(ai)
    bi=Decimal(bi)
    s.append([-ai/(ai+bi),i+1])
    
s.sort(key=lambda x: x[0])

for i in range(n):
    print(s[i][1],end=' ')