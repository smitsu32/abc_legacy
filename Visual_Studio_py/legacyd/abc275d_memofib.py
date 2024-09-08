from functools import lru_cache

@lru_cache(maxsize=None)  # メモ化再帰　フィボナッチ数列のO削減
def f(i):
    if i==0:
        return 1
    else:
        return f(i//2)+f(i//3)  # 高々O(log2(n)*log3(n))

n=int(input())
print(f(n))