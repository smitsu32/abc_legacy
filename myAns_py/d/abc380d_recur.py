# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

s=input()
q=int(input())
K=list(map(int,input().split()))

# k：文字数 l:レベル b:bool(大小文字入れ替えがb%2==1)
def f(k,l):
    global b
    if l==0:
        return s[k-1]
    else:
        h=len(s)<<(l-1) #レベルlの長さの半分
        if k<=h:
            return f(k,l-1) #b+=1で大小入れ替えるだけ
        else:
            b+=1
            return f(k-h,l-1) #長さ半分に

ans=[]
for i in range(q):
    b=0
    ansi=f(K[i],100) #2^100>1000^10>>10^18
    if b%2==1:
        ansi=chr(ord(ansi)^32) # 大文字小文字入れ替え(A=65,a=97より6bit目(=2^6)をXORをとる)
    ans.append(ansi)

print(*ans)