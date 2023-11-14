from collections import deque

n = int(input())

arr = []
for _ in range(n):
    tmp = list(input())
    arr.append(tmp)

k = int(input())
# 시작위치 구하기
sy, sx, head = 0,0,0

if k/n <=1:
    sy = 0
    sx = k-1
    head = 'fromN'

elif k/n <=2:
    sy = k - n - 1
    sx = n-1
    head = 'fromE'

elif k/n <=3:
    sy = n-1
    sx = k - 2*n -1
    head = 'fromS'

elif k/n <=4:
    sy = k - 3*n -1
    sx = 0
    head = 'fromW'

q = deque()
q.append([sy, sx, head])
cnt = 0

while q:
    y, x, head = q.popleft()
    cnt += 1
    if arr[y][x] == '\\':
        if head == 'fromN':  # 북쪽에서 오면
            dy = y
            dx = x + 1
            head = 'fromW'
        elif head == 'fromS':  # 남쪽에서 오면
            dy = y
            dx = x - 1
            head = 'fromE'
        elif head == 'fromE':  # 동쪽에서오면
            dy = y - 1
            dx = x
            head = 'fromS'
        elif head == 'fromW':  # 서쪽에서오면
            dy = y + 1
            dx = x
            head = 'fromN'

    elif arr[y][x] == '/':
        if head == 'fromN':  # 북쪽에서 오면
            dy = y
            dx = x - 1
            head = 'fromE'
        elif head == 'fromS':  # 남쪽에서 오면
            dy = y
            dx = x + 1
            head = 'fromW'
        elif head == 'fromE':  # 동쪽에서오면
            dy = y + 1
            dx = x
            head = 'fromN'
        elif head == 'fromW':  # 서쪽에서오면
            dy = y - 1
            dx = x
            head = 'fromS'

    if dy < 0 or dx < 0 or dy >= n or dx >= n:
        print(cnt)
        exit()

    q.append([dy, dx, head])