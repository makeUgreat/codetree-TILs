diy = [0,1,0,-1]
dix = [1,0,-1,0]


direction = {
    'N': 3,
    'E': 0,
    'S': 1,
    'W': 2
}

n = int(input())
y,x = 0,0
time = 0
for _ in range(n):
    command,dist = input().split()
    dist = int(dist)
    

    for i in range(dist):
        dy = y + diy[direction[command]]
        dx = x + dix[direction[command]]
        time += 1

        if dy == 0 and dx == 0:
            print(time)
            exit()

        y = dy
        x = dx 
        
        
print(-1)