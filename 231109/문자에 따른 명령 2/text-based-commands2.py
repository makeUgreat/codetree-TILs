commands = input()
y,x = 0,0
dir_num = 0

diy = [1,0,-1,0]
dix = [0,1,0,-1]


for command in commands:
    if command == 'F':
        y += diy[dir_num]
        x += dix[dir_num]
    
    if command == 'L':
        dir_num = (dir_num-1 + 4) % 4 

    if command == 'R':
        dir_num = (dir_num + 1) % 4

print(x,y)