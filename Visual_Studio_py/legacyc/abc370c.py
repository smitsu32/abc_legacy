s=input()
t=input()
n=len(s)

X=[]
while s!=t:     # 一致するまで全探索を繰り返す
    x='{'*n
    for i in range(n):
        if s[i]!=t[i]:
            x=min(x,s[:i]+t[i]+s[i+1:])     # copyがめんどいので変数はそのまま使う
    X.append(x)                             # 辞書順に小さいものをピックアップ
    s=x

print(len(X))
for i in X:
    print(i)