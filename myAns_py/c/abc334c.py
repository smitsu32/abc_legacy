n,k=map(int,input().split())
a=set(list(map(int,input().split())))

s=[]    # 靴下[1,1,2,3,3,4,4,5,5]
for i in range(1,n+1):
    s.append(i)
    if i not in a:
        s.append(i)
m=len(s)

if m%2==0:  #偶数:昇順に全て合わせる
    ans=0
    for i in range(m//2):
        ans+=s[2*i+1]-s[i*2]
    print(ans)
    exit()

else:       #奇数:左右から差の累積和
    si=0
    s1,s2=[0],[0]
    for i in range(m//2):
        si+=s[i*2+1]-s[i*2]
        s1.append(si)
    si=0
    for i in range(m//2-1,-1,-1):   
        si+=s[i*2+2]-s[i*2+1]   #終点+1（n:奇数）
        s2.append(si)
    
    ans=10**18
    for i in range(len(s1)):    # 0 ~ m//2+1
        ans=min(ans,s1[i]+s2[m//2-i])   #どれ余らすか

print(ans)