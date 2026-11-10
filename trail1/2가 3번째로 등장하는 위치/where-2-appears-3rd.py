N = int(input())

nums = list(map(int,input().split()))

idx = 0
num_idx = 0

for num in nums:
    if num == 2:
        num_idx += 1
    idx += 1
    if num_idx == 3:
        print(idx)
        break