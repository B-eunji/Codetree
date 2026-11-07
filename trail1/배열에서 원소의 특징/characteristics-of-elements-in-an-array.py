arr = list(map(int, input().split()))

idx = 0
for i in arr:
    if i % 3 == 0:
        print(arr[idx-1])
        break
    idx += 1