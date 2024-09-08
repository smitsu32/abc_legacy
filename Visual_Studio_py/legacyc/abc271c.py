# あるのは1cost, ないのは2costとしてansに加算
n=int(input())
a=set(list(map(int,input().split())))

ans,i=0,1
while True:
    if i not in a:
        ans+=1
    
    if 1+ans<=n:
        ans+=1
        i+=1
    else:
        print(i-1)  # １個オーバーしてる
        exit()