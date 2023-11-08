n,m = map(int,input().split())

time_a = [0]
for i in range(1,n+1):
    v,t = map(int,input().split())
    for j in range(t):
        time_a.append(time_a[j-1] + v)

time_b = [0]
for i in range(1,m+1):
    v,t = map(int,input().split())
    for j in range(t):
        time_b.append(time_b[j-1] + v)


# 길이(전체 시간) 맞추기
if len(time_a) >= len(time_b):
    longer = time_a
    lower = time_b
else:
    longer = time_b
    lower = time_a

gap = len(longer) - len(lower)
lower_last = lower[-1]
for _ in range(gap):
    lower.append(lower_last)

# print(time_a)
# print(time_b)

head = 0
cnt = 0
for i in range(len(longer)):
    
    if time_a[i] > time_b[i]:
        if head == 'a': continue
        head = 'a'
        cnt += 1

    elif time_a[i] < time_b[i]:
        if head == 'b': continue
        head = 'b'
        cnt += 1

print(cnt)