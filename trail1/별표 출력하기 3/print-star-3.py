N = int(input())
for i in range(N, 0, -1):
    for _ in range(N - i):
        print('  ', end = "")
    
    
    for j in range(2 * i - 1):
        print('* ',end="")
    
    

    
    print()
    