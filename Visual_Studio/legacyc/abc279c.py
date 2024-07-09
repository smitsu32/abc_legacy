# O(1.6*10^6)
h,w=map(int,input().split())
s=[input() for _ in range(h)]
t=[input() for _ in range(h)]

st=[[row[i] for row in s] for i in range(len(s[0]))]    # 転置（by ChatGPT）
tt=[[row[i] for row in t] for i in range(len(t[0]))]    # O(h*w)

s1=[''.join(row) for row in st] # [['#'],['.']][['#'],['.']] = ['#.','#.']
t1=[''.join(row) for row in tt] # 二次元リストを１次元に圧縮 O(h*w)
s1.sort()
t1.sort()

for i in range(w):
    if s1[i]!=t1[i]:
        print('No')
        exit()

print('Yes')