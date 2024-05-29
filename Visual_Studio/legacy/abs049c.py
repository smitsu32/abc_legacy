#ABS 白昼夢 erの扱いに注意
s=input()
b=''; c=''
for i in range(len(s)):
    b+=s[i]
    
    if b=='dream':
        if len(s)-i-1<2:
            b=''
        elif len(s)-i-1==2 and s[i+1]=='e' and s[i+2]=='r':
            continue
        elif s[i+1]=='e' and s[i+2]=='r' and s[i+3] in ('d','e'):
            continue
        else: b=''
    elif b=='erase':
        if len(s)-i-1<1:
            b=''
        elif len(s)-i-1>=1 and s[i+1]=='r':
            continue
        else: b=''
    elif b=='dreamer' or b=='eraser':
        b=''

if b!='': print('NO')
else: print('YES')