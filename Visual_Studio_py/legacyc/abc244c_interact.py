import sys

n=int(input())
print(2*n+1)

for i in range(n):
    i=int(input())
    if i%2==0:
        print(i-1)
    else:
        print(i+1)
    sys.stdout.flush()  # 出力をフラッシュ