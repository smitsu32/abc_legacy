s=[int(i) for i in input()]

t=s[::-1]
ans=0
now=0
for i in range(len(t)):
    if t[i]>=now:
        ans+=t[i]-now
        now=t[i]
    else:
        ans+=t[i]+10-now
        now=t[i]

print(ans+len(s))