h,w,n=map(int,input().split())
A,B=[],[]
for i in range(n):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

a={x:i+1 for i,x in enumerate(sorted(list(set(A))))}
b={x:i+1 for i,x in enumerate(sorted(list(set(B))))}

for i in range(n):
    print(a[A[i]],b[B[i]]) #圧縮座標