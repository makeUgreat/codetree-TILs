import sys, itertools

n = int(input())
cows = list(map(int, input().split()))
cases = [i for i in range(n)]
permutation = itertools.permutations(cases,3)

cnt = 0
for p in permutation:

    if p[0] < p[1] < p[2]:
        if cows[p[0]] < cows[p[1]] < cows[p[2]]:
            cnt += 1

print(cnt)