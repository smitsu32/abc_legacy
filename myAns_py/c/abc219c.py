from collections import deque

x,n=input(),int(input())
s=[input() for _ in range(n)]
pos=[0]*26
for i in range(26):
    j=ord(x[i])-97
    pos[j]=i

t=[]
for i in range(n):
    ti=[]
    for j in range(len(s[i])):
        ti.append(pos[ord(s[i][j])-97])
    t.append([ti,i])
t.sort(key=lambda x:x[0])

for i in range(n):
    print(s[t[i][1]])