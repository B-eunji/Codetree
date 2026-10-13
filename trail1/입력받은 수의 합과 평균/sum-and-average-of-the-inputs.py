N = int(input())

sum = 0
cnt = 0


for _ in range(N):
    num = int(input())
    sum += num
    cnt += 1

avg = sum/cnt
print(f"{sum} {avg:.1f}")