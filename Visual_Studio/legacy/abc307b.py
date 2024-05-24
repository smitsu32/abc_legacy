# ABC307b 任意のs[i]の合成文字列tは回文か？
n=int(input())
s=[input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j: continue
        t=s[i]+s[j]
        
        frag=True
        for k in range(len(t)//2):
            if t[k]!=t[-k-1]: frag=False
        if frag: exit(print('Yes'))
print('No')