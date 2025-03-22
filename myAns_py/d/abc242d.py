import sys
sys.setrecursionlimit(10**6)

s,q=input(),int(input())

def abc(t,k):
    a=ord(s[0])-65
    if t==0:    # 初期値
        return ord(s[k])-65
    if k==0:    # 012012...で推移する（s[0]は0とは限らない）
        return (a+t)%3
    
    #0  1   2
    #01 20  01
    # 直下(%=0)ならt-1に+1,1進み(%=1)ならt-1に+2
    if k%2==0:
        return abc(t-1,k//2)+1
    else:
        return abc(t-1,k//2)+2

for _ in range(q):
    t,k=map(int,input().split())
    k-=1        # abcに入れると再帰のたび-1されるためダメ
    ans=abc(t,k)%3  # ABCのみにしたいから
    print(chr(ans+65))