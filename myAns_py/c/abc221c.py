from itertools import *

n=list(input())
ans=0
for l in list(permutations(n)):
    for i in range(1,len(n)):
        if l[i]=='0': continue
        
        ansi=int(''.join(l[:i]))*int(''.join(l[i:]))
        # print(l[:i],l[i:])
        ans=max(ans,ansi)

print(ans)