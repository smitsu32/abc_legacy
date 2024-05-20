# ABC326B 桁ごとの乗算
n=input()
for i in range(820):
    if int(n[0])*int(n[1])==int(n[2]):
        exit(print(n))
    temp=int(n)+1; n=str(temp)

## intのまま解く方法
# n=int(input())
# for _ in range(820):
#     if n//100*(n%100//10)==n%10: exit(print(n))
#     n+=1