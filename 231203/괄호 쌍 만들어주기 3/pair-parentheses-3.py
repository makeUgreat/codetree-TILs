words = list(input())

start = 0
cnt = 0
for i in range(len(words)):

    if words[i] == '(':
        start = i
        for j in range(start,len(words)):
            if words[j] == ')':
                cnt += 1

print(cnt)