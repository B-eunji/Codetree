n = int(input())

cnt = 0

for num in range(1, n+1):
    if num % 2 == 0:
        continue
    elif num % 10 == 5 or num % 100 == 5:
        continue
    elif num % 3 == 0 and num % 9 != 0:
        continue
    print(num, end = " ")