s,t=input().split()

for i in range(1,len(s)):
    for k in range(0,i):
        a=''
        for j in range(1,len(s)+1):
            if (i*j)-k-1>=len(s): continue
            a+=s[(i*j)-k-1]
        # print(i,a)
        if a==t:
            print('Yes')
            exit()

print('No')