n=int(input())
s=list(input())

flag=False
for i in range(n):
    if flag:
        if s[i]=='\"':  # \ 注意
            flag=False
    else:
        if s[i]=='\"':
            flag=True
        elif s[i]==',':
            s[i]='.'

print(*s,sep='')