s=input()
n=len(s)

b,c=0,0
for i in range(n):
    if s[i]=='a':
        b+=1
    else: break
for i in range(n):
    if s[n-i-1]=='a':
        c+=1
    else: break

if b==n:    # 必須
    print('Yes')
    exit()
if b>c:
    print('No')
    exit()

t=s[:n-(c-b)]
if t==t[::-1]:
    print('Yes')
else:
    print('No')