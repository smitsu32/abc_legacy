s=list(input())
at=['a','t','c','o','d','e','r']

for i in range(7):
    for j in range(7):
        if s[i]==at[j]:
            s[i]=j

a=0
# bubble sort
for i in range(7):#数字 6~0
    for j in range(7-1-i):#index 0~6,6確定,0~5,5確定, ...
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
            a+=1
print(a)