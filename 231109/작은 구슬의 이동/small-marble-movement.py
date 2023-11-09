n, t = map(int, input().split())
y, x, head = input().split()
y, x = int(y), int(x)

arr = [[0] * n for _ in range(n)]
diy = [1, 0, 0, -1]
dix = [0, 1, -1, 0]
direct = {
    'U': 0,
    'D': 3,
    'R': 1,
    'L': 2
}

dir_num = direct[head]
for _ in range(t):
    # print(y,x)
    dy = y + diy[dir_num]
    dx = x + dix[dir_num]
    if dy < 1 or dx < 1 or dy >= n+1 or dx >= n+1:
        dir_num = 3 - dir_num
        continue

    x = x + dix[dir_num]
    y = y + diy[dir_num]

print(y, x)