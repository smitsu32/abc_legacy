import sys
sys.setrecursionlimit(10**7)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

n,q=map(int,input().split())

S=[(-1, "")] # 文字列で保存
P=[0]*n # id
now=1 # 現在の編集id
sur=0 # サーバーid

for _ in range(q):
    qu=input().split()
    if qu[0]=='1':
        p=int(qu[1])
        P[p-1]=sur
    elif qu[0]=='2':
        p=int(qu[1])
        s=qu[2]
        S.append((P[p-1], s))  # 文字列で保存
        P[p-1]=now
        now+=1
    else:
        p=int(qu[1])
        sur=P[p-1] # サーバーidを更新 昔のものはSに残る

def f(i): # サーバーを出力する→最後からidをたどって復元
    r=[] # サーバー
    j=i
    while j!=-1: # たどれる限りたどる
        p,s = S[j] # (親id, 文字列)
        r.append(s)
        j=p
    return "".join(reversed(r))

print(f(sur))