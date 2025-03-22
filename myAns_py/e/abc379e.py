n=int(input())
s=input()

a=[(i+1)*int(s[i]) for i in range(n)] #桁ごとに累積和[... ,100,10,1の位]
for i in range(1,n):
    a[i]+=a[i-1]
# print(a)

i,c=0,0 #index, その桁の数

ans=[] #ひっ算で
a.reverse()

while i<n or c>0: #c=100のように最上位から2つ上の桁に行くこともあるためc>0も
    if i<n:
        c+=a[i]
    ans.append(c%10)
    c//=10
    i+=1

print(*ans[::-1],sep='') #逆順に