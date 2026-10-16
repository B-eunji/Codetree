total = 0
cnt = 0

while True:
    age = int(input())
    if age//10 != 2:
        break
    total += age
    cnt += 1

avg = total/cnt
print(f"{avg:.2f}")

