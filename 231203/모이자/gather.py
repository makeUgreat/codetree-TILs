import sys

n = int(input())
people = list(map(int, input().split()))

min_ = sys.maxsize
for i in range(n):
    sum_ = 0
    for j in range(n):
        diff = abs(i - j)
        sum_ += people[j] * diff


    min_ = min(sum_, min_)

print(min_)