diy = [0,-1,0,1] #북 남
dix = [-1,0,1,0] #좌 우  
dir_num = 1  # 북쪽 바라보고 시작

commands = input()

y,x = 0,0
time = 0
for command in commands:
    if command == 'R':
        dir_num = (dir_num + 1) % 4
    
    elif command == 'L':
        dir_num = ((dir_num + 4) -1) % 4
    
    elif command == 'F':
        y = y + diy[dir_num]
        x = x + dix[dir_num]
    
    time += 1

    if y == 0 and x == 0:
        print(time)
        exit()
print(-1)