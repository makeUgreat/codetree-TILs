n,m = map(int,input().split())

arr = [[0]*(n+1) for _ in range(n+1)]

def check(y,x):
    diy = [0,-1,0,1]
    dix = [1,0,-1,0]
    cnt = 0

    for i in range(4):
        dy = y+diy[i]
        dx = x+dix[i]
        if dy<1 or dx<1 or dy>=n+1 or dx>=n+1: continue
        if arr[dy][dx] == 1:
            cnt += 1
    
    if cnt == 3:
        return 1
    else:
        return 0

for _ in range(m):
    y,x = map(int,input().split())
    arr[y][x] = 1

    if check(y,x):
        print(1)
    else:
        print(0)