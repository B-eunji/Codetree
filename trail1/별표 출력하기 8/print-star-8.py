N = int(input())

for i in range(1, N+1):
    if i % 2 == 0:
        for _ in range(i):
            print('* ', end="")
    else:
        print('* ',end="")

    print()