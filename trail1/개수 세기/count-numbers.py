N, M = map(int, input().split())
cnt = 0

for num in map(int, input().split()):
    if num == M:
        cnt += 1

print(cnt)