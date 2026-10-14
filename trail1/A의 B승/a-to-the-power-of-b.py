A, B = map(int, input().split())

result = 1

for num in range(B):
    result *= A

print(result)