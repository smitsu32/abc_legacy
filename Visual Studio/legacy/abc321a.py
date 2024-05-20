" ABC321 a"

n = input()
num = len(n)
intn = list(map(int, n))

for i in range(num-1):
    if intn[i] <= intn[i+1]:
        print("No")
        exit()

print("Yes")