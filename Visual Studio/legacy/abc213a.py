# ABC213A 2進数の引き算XOR
a,b=map(int,input().split())
# ^ はビットごとにXORを返し10進数に変換する（01,10->1  11,00->0）
print(a^b)
