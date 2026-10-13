A, B = map(int, input().split())

total = 0

if A>B:
    for num in range(B, A+1):
        if num % 5 == 0:
            total += num
elif B>A:
    for num in range(A, B+1):
        if num % 5 == 0:
            total += num
else:
    for num in range(B, A+1):
        if num % 5 == 0:
            total += num

print(total)

