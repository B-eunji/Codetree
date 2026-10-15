A = int(input())

result = 0

for num in range(1, A+1):
    if num % 2 == 0 and num % 4 != 0:
        continue
    elif (num // 8) %2 == 0: 
        continue
    elif num % 7 < 4:
        continue
    
    print(num, end = " ")