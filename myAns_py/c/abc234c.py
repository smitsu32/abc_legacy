k=int(input())
temp=''
for i in range(k):
    temp+=str(k%2)
    k//=2
    if k==0:
        break

temp=temp[::-1]
ans=''
for i in range(len(temp)):
    ans+=str(int(temp[i])*2)
print(int(ans))