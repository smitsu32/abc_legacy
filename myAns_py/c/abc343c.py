from math import log
n=input()

ans=1
for i in range(1,10**6+1):     # 3乗の数を比べる
    i**=3
    if i>int(n): break
    
    flag=True
    i=str(i)
    for j in range(len(i)):
        if i[j]!=i[len(i)-j-1]:
            flag=False; break
    
    if flag:
        ans=i

print(ans)