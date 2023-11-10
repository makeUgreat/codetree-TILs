n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

diy = [0, 1, 0, -1]
dix = [1, 0, -1, 0]

dir_num = 0

def in_range(y,x):
    return x >= 0 and x < n and y >= 0 and y < n

y,x= 0,0
arr[0][0] = 1
for i in range(2,n*m+1):
    dy = y + diy[dir_num]
    dx = x + dix[dir_num]

    if not in_range(dy,dx) or arr[dy][dx] != 0:
        dir_num = (dir_num+1) % 4

    y = y + diy[dir_num]
    x = x + dix[dir_num]
    arr[y][x] = i


for a in arr:
    print(*a)