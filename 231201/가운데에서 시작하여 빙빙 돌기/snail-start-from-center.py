n = int(input())
cnt = n*n

grid = [[0]*n for _ in range(n)]
grid[n-1][n-1] = cnt 

y,x = n-1, n-1
diy = [0,-1,0,1]
dix = [-1,0,1,0]
idx = 0
while cnt > 1:
    dy = y + diy[idx]
    dx = x + dix[idx]
    if dy<0 or dx<0 or dy>=n or dx>=n or grid[dy][dx] != 0:
        idx = (idx+1) % 4
        continue

    y,x = dy,dx 
    cnt -= 1
    grid[y][x] = cnt

    

for g in grid:
    print(*g)