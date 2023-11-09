n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
diy = [-1,0,1,0]
dix = [0,1,0,-1]

def check(y,x):
    global total
    sy,sx = y,x 
    cnt = 0
    for i in range(4):
        dy = y + diy[i]
        dx = x + dix[i]
        if dy<0 or dx<0 or dy>=n or dx>=n: continue
        if arr[dy][dx] == 1:
            cnt += 1
            if cnt >= 3:
                total += 1
                return         

            

                


    

total = 0
for i in range(4):
    for j in range(4):
        check(i,j)

print(total)