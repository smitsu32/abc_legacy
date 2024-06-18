s=input().upper()
t=input()

# print(s,t)
flag1=False
flag2=False

for i in range(len(s)):
    if s[i]==t[0] and flag1==False:  # ないとt=XXRのとき2文字目が永遠に処理されなくなる
        flag1=True
        # print(i+1)
    elif s[i]==t[1] and flag1 and flag2==False:
        flag2=True
        # print(i+1)
        if t[2]=='X': exit(print('Yes'))
    elif s[i]==t[2] and flag2:
        # print(i+1)
        exit(print('Yes'))

print('No')