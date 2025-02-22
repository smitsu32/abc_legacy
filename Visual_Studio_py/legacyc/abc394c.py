s=list(input())
n=len(s)
s=s[::-1]

w=[]
for i in range(len(s)):
    if s[i]=='W':
        w.append(i)

for i in w:
    if i==0: continue
    if s[i-1]=='A':
        s[i]='A'
        s[i-1]='C'

print(''.join(s[::-1]))