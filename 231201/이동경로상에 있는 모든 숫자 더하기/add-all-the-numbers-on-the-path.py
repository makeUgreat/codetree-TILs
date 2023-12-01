n, t = map(int, input().split())
command = list(input())
grid = [list(map(int, input().split())) for _ in range(n)]
y, x = n//2, n//2


diy = [-1, 0, 1, 0]
dix = [0, 1, 0, -1]
idx = 0
sum_ = grid[y][x]

# print(sum_, grid[y][x],y,x)

for c in command:
    if c == 'R':
        idx = (idx + 1) % 4

    elif c == 'L':
        idx = (idx - 1) % 4

    elif c == 'F':

        dy = y + diy[idx]
        dx = x + dix[idx]
        if dy < 0 or dx < 0 or dy >= n or dx >= n: continue

        sum_ += grid[dy][dx]
        y,x = dy,dx

        # print(sum_, grid[y][x],y,x)

print(sum_)