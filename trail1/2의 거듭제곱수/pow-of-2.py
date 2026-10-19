N = int(input())
x = 1

while x <= 10:
    if 2**x == N:
        print(x)
        break
    x += 1
    
