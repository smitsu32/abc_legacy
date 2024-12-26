s=list(input())

t=s[::-1]
a=0
for i in range(len(t)):
    if t[i]=='a':
        a+=1
    else:
        break

if a==0:
    if s==s[::-1]:
        print('Yes')
    else:
        print('No')
    exit()

for i in range(1,a+1):
    t=['a'*i]+s
    if t==t[::-1]:
        print('Yes')
        exit()
print('No')