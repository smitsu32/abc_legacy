from functools import cache
n=int(input())

# n=[n//2, (n-1)//2+1]  # 1回の処理
# ans=n

@cache                  # メモ化再帰->結果をメモ,重複処理をなくし高速化
def div(n):
    if n==1: return 0   # n!=1でも再帰内でdev(1)が必要
    else:
        return div(n//2)+div((n-1)//2+1)+n

print(div(n))