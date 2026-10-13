sum = 0
cnt = 0

for _ in range(10):
    num = int(input())
    if (num >= 0 and num <= 200):
        cnt += 1
        sum += num

avg = sum / cnt

print(f"{sum} {avg:.1f}")