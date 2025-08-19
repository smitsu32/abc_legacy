from bisect import bisect_left, bisect_right

T=int(input())

for _ in range(T):
    n=int(input())
    s=list(map(int, input().split()))
    
    if s[0]>=s[-1]:
        print(2)
        continue
    
    t=set()
    for i in range(n):
        if s[0]<=s[i]<=s[-1]:
            t.add(s[i])
    t=sorted(t) # これだけでリストに変換
    
    now=t[0]
    ans=1 # ドミノ1
    while 2*now<t[-1]:
        next=bisect_right(t, 2*now)-1
        if next>=len(t)-1 or next<0:
            ans=-1
            break
        if t[next]<=now:
            ans=-1
            break
        ans+=1
        now=t[next]
    
    if ans==-1:
        print(-1)
    else:
        print(ans+1)