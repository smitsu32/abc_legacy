## math は　平方根、π、三角比　で使用
import math

## 1-1 数値演算
# print("Hallo, World")

# print(2**100)
# print(2*1e30)
# print((9-1)/4)
# print(9//4)
# print(9%4)
# print(4*(3/8),'\n')

# print(4**2**3)
# print(4**(2**3))

# print(int(3.5))
# print(float(2))

# print(math.sqrt(3))
# print(math.sin(1))
# print(math.sin(math.pi/2))
# print((math.sqrt(5)+1)/2) ##黄金比

## 1-2 変数と関数の基礎
# h=188.0
# h -= 63
# print(h//2)

# def bmi(height, weight):                  ## 関数の作り方 def
#     return weight / (height/100.0)**2

# print(bmi(174.9, 59.2))
# print(1.0*bmi(174.9, 29.6*2))

# def ft_to_cm(f, i):
#     return (f*12+i)*30.48/12

# assert round(ft_to_cm(5, 2) - 157.48, 6) == 0
# assert round(ft_to_cm(6, 5) - 195.58, 6) == 0

# def quadratic(a, b, c, x):
#     return a*x**2+b*x+c

# assert quadratic(1, 2, 1, 3) == 16
# assert quadratic(1, -5, -2, 7) == 12

# # heronの公式により三角形の面積を返す
# def heron(a,b,c): # a,b,c は三辺の長さ

#     # 辺の合計の半分をsに置く
#     s = 0.5*(a+b+c)
#     print('The value of s is', s)

#     return math.sqrt(s * (s-a) * (s-b) * (s-c))

# print(heron(2,3,4))

## 練習
# def qe_disc(a,b,c):
#     return b**2-4*a*c
# def qe_solution1(a,b,c):
#     return (-b-math.sqrt(qe_disc(a,b,c)))/(2*a)
# def qe_solution2(a,b,c):
#     return (-b+math.sqrt(qe_disc(a,b,c)))/(2*a)

# assert qe_disc(1, -2, 1) == 0                     ## Falseでエラー
# assert qe_disc(1, -5, 6) == 1
# assert round(qe_solution1(1, -2, 1) - 1, 6) == 0
# assert round(qe_solution2(1, -2, 1) - 1, 6) == 0
# assert round(qe_solution1(1, -5, 6) - 2, 6) == 0
# assert round(qe_solution2(1, -5, 6) - 3, 6) == 0

# g=9.8
# def force(m):
#     print(g)
#     return m*g

# print(force(104))


## 1-3 論理・比較演算と条件分岐の基礎
# def bmax(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
        
# bmax(6,2)

# print(2>1 or 3<2)

## 練習 abs
# def absolute(x):
#     if x>0:
#         return x
#     return -x

# assert absolute(5) == 5
# assert absolute(-5) == 5
# assert absolute(0) == 0

# print(max(1,3))


## 練習 sin(x)
# def sign(x):
#     if x>0:
#         return 1
#     elif x<0:
#         return -1
#     else:
#         return 0

# assert sign(5) == 1
# assert sign(-5) == -1
# assert sign(0) == 0

# def is_even(x):
#     return x % 2 == 0

# def is_odd(x):
#     if is_even(x):
#         return False
#     else:
#         return True

# print(is_odd(4))

# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-2) + fib(n-1)

# print(fib(20))


## 1-4 テストとデバッグ
# def square(x):
#     return x*x

# x = -2
# assert square(x) == 4

# def median(x,y,z):
#     if x > y:
#         w = x
#         x = y
#         y = w
#     if z < y:
#         return z
#     return y

# assert median(3,1,2) == 2

