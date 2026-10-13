A, B = map(int, input().split())

sum = 0
cnt = 0

for num in range(A, B+1):
    if(num % 5 == 0):
        sum += num
        cnt += 1
    elif(num % 7 == 0):
        sum += num
        cnt += 1

avg = sum/cnt

print(f"{sum} {avg:.1f}")