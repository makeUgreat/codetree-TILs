n, m = map(int, input().split())

grid = [[0] * m for _ in range(n)]
grid[0][0] = 'A'
y, x = 0, 0

diy = [0, 1, 0, -1]
dix = [1, 0, -1, 0]
idx = 0
cnt = 0
t = 0
while t < n*m-1:
    dy = y + diy[idx]
    dx = x + dix[idx]
    if dy < 0 or dx < 0 or dy >= n or dx >= m:
        idx = (idx + 1) % 4
        continue
    if grid[dy][dx] != 0:
        idx = (idx + 1) % 4
        continue

    y, x = dy, dx

    cnt = (cnt + 1) % 26
    grid[y][x] = chr(cnt + ord('A'))
    t += 1

for g in grid:
    print(*g)