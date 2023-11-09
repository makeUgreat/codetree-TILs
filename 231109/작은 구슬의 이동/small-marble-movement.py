n, t = map(int, input().split())
y,x, head = input().split()
y, x = int(y), int(x)

arr = [[0] * n for _ in range(n)]
diy = [1, 0, 0, -1]
dix = [0, 1, -1, 0]
direct = {
    'U': 3,
    'D': 0,
    'R': 1,
    'L': 2
}

dir_num = direct[head]
for now in range(1,t+1):
    dy = y + diy[dir_num]
    dx = x + dix[dir_num]
    if dy < 1 or dx < 1 or dy >= n+1 or dx >= n+1:
        dir_num = 3 - dir_num
        # print(f'{now}초: {y},{x} 방향전환')
        continue

    x = x + dix[dir_num]
    y = y + diy[dir_num]
    # print(f'{now}초: {y},{x}')

print(y,x)