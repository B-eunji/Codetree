A, B = map(int, input().split())

result = 1

for num in range(1, B+1):
    if num % A == 0:
        result *= num

print(result)