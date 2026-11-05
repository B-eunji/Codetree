arr = list(map(int, input().split()))

result = 0
avg_total = 0

n = len(arr)

for a in arr[1::2]:
    result += a
for b in range(2, n, 3):
    avg_total += arr[b]

avg = avg_total/3
print(result, f"{avg:.1f}")