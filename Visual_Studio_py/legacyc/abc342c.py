from copy import deepcopy
n=int(input()); s=input(); q=int(input())

al='abcdefghijklmnopqrstuvwxyz'
# al2=deepcopy(s)

for i in range(q):
    ci,di=input().split()
    al=al.replace(ci,di)
    
ans=''
for i in range(n):
    ans+=al[ord(s[i])-97]       # sのi文字目(a)をal[0]に置き換え

print(ans)