s=input()
l=len(s)

ansl=l*(l+1)//2          # 組み合わせ(Conbination)
ans=ansl

c=[0]*26
for i in range(len(s)):
    c[ord(s[i])-97]+=1

flag=False
for i in range(26):     # 重複を除きたい->aaaならこの並び替えを除外
    cc=c[i]
    ans-=cc*(cc+1)//2   # 1こでも-1 
    if cc>=2: flag=True

if flag:        # anslは２回重複している
    ans+=1              # 入れ替えた場合足す(すべて異なるときは引かれていないため無視)

print(ans)