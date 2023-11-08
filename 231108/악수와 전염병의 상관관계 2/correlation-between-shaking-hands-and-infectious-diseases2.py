N, K, P, T = map(int, input().split())

infection = [0] * (N + 1)
infection[P] = 1

time = [[0, 0] for _ in range(251)]
cnt_check = [0] * (N + 1)
for _ in range(T):
    t, x, y = map(int, input().split())
    time[t] = [x, y]

for a, b in time:
    if a == 0 and b == 0: continue

    if infection[a] == 1 and infection[b] == 0:
        if cnt_check[a] < K:
            cnt_check[a] += 1
            infection[b] = 1
            # cnt_check[b] += 1

    elif infection[a] == 0 and infection[b] == 1:
        if cnt_check[b] < K:
            cnt_check[b] += 1
            infection[a] = 1
            # cnt_check[a] += 1

    elif infection[a] == 1 and infection[b] == 1:
        cnt_check[a] += 1
        cnt_check[b] += 1

    # print(a,b,infection[1:])

print(*infection[1:], sep='')