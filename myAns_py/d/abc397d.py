# x^3-y^3   = (x-y)(x^2+xy+y^2)
#          >= (x-y)(x^2-2xy+y^2) = (x-y)^3

# therefore (x-y)^3 <= N
#           d <= N^1/3

# (k+d)^3-k^3 = N となる自然数kをd:1~N^1/3 で探索すればよい
# (与式) = 3dk^2+3d^2k+d^3-N = 0 を解く

n=int(input())

for i in range(1,round(n**0.34)+1): # d
    k=(-3*i**2+(12*i*n-3*i**4)**0.5)/(6*i)
    if k%1==0 and k>0:
        print(int(k+i),int(k))
        exit()

print(-1)