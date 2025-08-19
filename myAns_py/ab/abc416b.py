s=list(input())
n=len(s)

# ##間に1個oを　→　一番左と決め打てばよい
for i in range(n-1):
    if s[i]=='#' and s[i+1]=='.':
        s[i+1]='o'

if s[0]=='.':
    s[0]='o'

print(''.join(s))