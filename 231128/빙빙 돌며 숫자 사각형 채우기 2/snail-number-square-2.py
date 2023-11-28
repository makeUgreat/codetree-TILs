n,m = map(int,input().split())

grid = [[0] * m for _ in range(n)]

diy = [1,0,-1,0]
dix = [0,1,0,-1]  # 남동북서 반복

y,x = 0,0
grid[y][x] = 1
idx = 0
cnt = 1
while cnt < (n*m):
    dy = y + diy[idx]
    dx = x + dix[idx]
    if dy<0 or dx<0 or dy>=n or dx>=m:
        idx = (idx+1)%4
        continue
    if grid[dy][dx] != 0:
        idx = (idx+1)%4
        continue

    cnt += 1
    y,x = dy,dx
    grid[y][x] = cnt

for g in grid:
    print(*g)