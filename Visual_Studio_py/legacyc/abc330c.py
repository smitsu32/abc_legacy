d=int(input())

ans=10**12
# 円にx=i(整数)の線を重ねて縦に見ると...
for i in range(int(d**0.5)+1): # x<=sqrt(d)
    j=d-i**2
    
    if j>0:                 # 円がy!=0のどこかでx=iと交わる
        j1=int(j**0.5)
        j2=j1+1
        ans=min(ans,j-j1**2,j2**2-j)    # 円の上下点を比較
    
    elif j==0:                          # ちょうど円が(i,0)を通る->距離0
        ans=0
        break
    
    else:                   # 円がx=i上には存在しない->右端
        ans=min(ans,-j)     # jは円周のy=0の点と格子点の距離
        break
print(ans)