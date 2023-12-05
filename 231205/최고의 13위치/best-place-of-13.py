n = int(input())
grid = [ list(map(int,input().split())) for _ in range(n) ]


def check(y,x):
    cnt = 0
    for k in range(3):
        if grid[y][x+k] == 1:
            cnt += 1

    return cnt

max_ = 0
for i in range(n):
    for j in range(n-2):
        max_ = max(max_, check(i,j))

print(max_)