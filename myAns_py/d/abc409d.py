t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if n==1:
        print(s); continue
    
    l,r=0,n-1
    for i in range(n-1): # z a みたいになる最初の文字をできるだけ後ろに
        if ord(s[i])>ord(s[i+1]):
            l=i
            break
    
    for i in range(l,n-1):
        if ord(s[l])<ord(s[i+1]): # s[l]=x ,zだと入れ替えたら損なのでこの前まで
            r=i
            break
    print(s[:l]+s[l+1:r+1]+s[l]+s[r+1:])