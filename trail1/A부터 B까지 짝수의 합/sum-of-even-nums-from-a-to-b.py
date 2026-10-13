A, B = map(int, input().split())

sum = 0

for num in range(A, B+1):
    if num% 2 == 0:
        sum += num

print(sum)