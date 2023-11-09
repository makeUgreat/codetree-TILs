n = int(input())

diy = [1,-1,0,0]
dix = [0,0,-1,1]
direct = {
    'N': 0,
    'S': 1,
    'E': 3,
    'W': 2
}

y,x = 0,0
for _ in range(n):
    head, dist = input().split()
    dist = int(dist)

    y = y + diy[direct[head]] * dist
    x = x + dix[direct[head]] * dist
    

print(x,y)