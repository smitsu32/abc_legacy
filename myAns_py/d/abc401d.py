from itertools import groupby

n,k=map(int,input().split())
s=list(input())

cntO=s.count('o')

if cntO==k: # oが既にk個ある場合
    s=['.' if i=='?' else i for i in s]
    print(*s,sep='')
    exit()

s=['.']+s+['.'] # i+1,i-1の分岐をなくすため
for i in range(1,n+1): # ?o? を .o. に
    if s[i]=='o':
        s[i-1]='.'
        s[i+1]='.'
s=s[1:-1]

cntQ=s.count('?')

if k==cntO+cntQ: # 'o','?'の合計がk個の場合
    s=['o' if i=='?' else i for i in s]
    print(*s,sep='')
    exit()

# ランレングス圧縮
r=[(char,len(list(group))) for char,group in groupby(s)]

rep=0 # 置き換えられる?のMax数
for char,l in r:
    if char=='?':
        if l%2==0:
            rep+=l//2
        else:
            rep+=l//2+1

if cntO+rep>k: # oの候補が多い場合
    print(*s,sep='')
else: # oの候補数がちょうどの場合
    ans=[]
    for char,l in r:
        if char=='?' and l%2==1: # ?の数が奇数の場合
            ans.extend(['o','.']*(l//2)+['o'])
        else:
            ans.extend([char]*l)
    print(*ans,sep='')