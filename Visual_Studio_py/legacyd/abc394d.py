from collections import deque

s=list(input())
n=len(s)
d=deque()

if n%2==1:
    print('No')
    exit()

def check(si):
    if si==')' and d[-1]=='(':
        return True
    if s[i]==']' and d[-1]=='[':
        return True
    if s[i]=='>' and d[-1]=='<':
        return True

for i in range(n):
    # print(d,s[i])
    if s[i]=='(' or s[i]=='[' or s[i]=='<':
        d.append(s[i])
    elif d and check(s[i]):
        d.pop()

if not d:
    print('Yes')
else:
    print('No')
