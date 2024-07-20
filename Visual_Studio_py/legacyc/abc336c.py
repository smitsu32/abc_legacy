n=int(input())-1            # in:1がout:0だから

def b5(n):
    a0=n%5; n//=5
    a=str(a0)
    while True:
        if n==0: break
        a+=str(n%5); n//=5      # n進数変換は %nをstrで足してreverse
    a=a[::-1]
    return int(a)

print(b5(n)*2)