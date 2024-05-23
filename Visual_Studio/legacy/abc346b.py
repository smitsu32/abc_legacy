#ABC346 B 繰り返し中に部分文字列が含まれているか
def mp() : return map(int,input().split())

w,b = mp()
s = "wbwbwwbwbwbw" * 20

# wの残りがbになるため、数えるのはwのみ
# 12ごとにsが繰り返されるので、forは12通りでよい

for i in range(12):
    cw = s[i:i+w+b].count('w')
    # cb = s[i:n+1].count('b') 
    if cw == w: # and cb == b:
        print("Yes")
        exit()

print("No")