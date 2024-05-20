#ABC333B 5角形の辺の長さ判定
s=input(); t=input()
# ASKii-code出力
s1=ord(s[0]); s2=ord(s[1]); t1=ord(t[0]); t2=ord(t[1])

if abs(s1-s2)== abs(t1-t2):
    exit(print('Yes'))

# DEとAEは等しいため、A->A+5(F) として再判定
sd=min(s1,s2)+5; td=min(t1,t2)+5
if sd-max(s1,s2)==td-max(t1,t2):
    exit(print('Yes'))
elif abs(s1-s2)==td-max(t1,t2) or sd-max(s1,s2)==abs(t1-t2):
    exit(print('Yes'))

print('No')