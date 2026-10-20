N = int(input())

result = False

for i in range(2, N):
    if N % i == 0:
        result = True

if result == False:
    print("N")
else:
    print("C")