s,t=input(),input()
n,m=len(t),len(s)
sr,tr=s[::-1],t[::-1]

start,end=[False]*(len(t)+1),[False]*(len(t)+1)
start[0],end[0]=True,True   # endは逆順(nから)

flag1,flag2=True,True
for i in range(n):  # 最初のn文字、最後のn文字でそれぞれ同じか確認して最後に合わせる
    if (s[i]==t[i] or s[i]=='?' or t[i]=='?') and flag1:
        start[i+1]=True
    else:
        flag1=False
    
    if (sr[i]==tr[i] or sr[i]=='?' or tr[i]=='?') and flag2:
        end[i+1]=True   # 逆順ソートしてるので順に格納
    else:
        flag2=False

for i in range(n+1):
    if start[i] and end[-1-i]:
        print('Yes')
    else:
        print('No')