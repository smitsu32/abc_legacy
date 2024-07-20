# ABC331B 7,8,12個から最安の組み合わせ
## 処理量は高々O(10^3)なので余裕
n,s,m,l=map(int,input().split())
spjudge=10**15
for i in range(n//6+2):
    for j in range(n//8+2):
        for k in range(n//12+2):
            if i*6+j*8+k*12 >= n:
                sp=i*s+j*m+k*l
                if sp<spjudge:
                    spjudge=sp

print(spjudge)