n=int(input())
qr=[[]]
for _ in range(n):
    q,r=map(int,input().split())
    qr.append([q,r])

q=int(input())
for _ in range(q):
    t,d=map(int,input().split())
    q,r=qr[t]
    ans=((d-r-1)//q+1)*q    #割り切れるのを繰り下げる
    print(ans+r)