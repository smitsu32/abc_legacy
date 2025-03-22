n=int(input())
s=list(input())

def dango(s):       # 逆順でも使いたいから関数化
    flag=True
    ok=[]
    if s[0]=='o':
        ok.append(0)

    for i in range(1,n):
        if s[i-1]=='-' and s[i]=='o':
            ok.append(i)

    ans=-1
    for i in ok:
        for j in range(1,n-i):
            if s[i+j]=='-':
                ans=max(ans,j)
                break
    return ans

t=s[::-1]

print(max(dango(s),dango(t)))