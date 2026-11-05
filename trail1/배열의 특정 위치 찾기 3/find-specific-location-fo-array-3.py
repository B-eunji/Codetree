arr = list(map(int, input().split()))

total = 0
idx = 0


for a in arr:
    if a == 0:
        total = arr[idx-1] + arr[idx-2] + arr[idx-3]
        break
    idx += 1
print(total)

