N = int(input())

for i in range(2 * N):
    if i % 2 == 0:
        for _ in range(i // 2 + 1):
            print("* ", end="")
    else:
        for _ in range(N - (i - 1) // 2):
            print("* ", end="")

    print()