n=int(input())
ac=[]

for i in range(n):
    aci=list(map(int,input().split()))
    ac.append(aci)

ac.sort(key=lambda x: x[1])     # cで２次元ソート

nowc=ac[0][1]                   # cは同じ値か判定する
a,ans=[],[]
for i in range(n):
    if i==n-1:                  # 最後にansに代入
        a.append(ac[i][0])
        ans.append(min(a))
        break
    
    if ac[i][1]==nowc:          # cが前のと同じとき
        a.append(ac[i][0])
    else:
        ans.append(min(a))      # 違うときaのmin処理してリセット
        nowc=ac[i][1]
        a=[ac[i][0]]

print(max(ans))