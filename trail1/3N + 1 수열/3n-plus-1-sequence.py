cnt = 0
N = int(input())

while (N != 1):
    if N % 2 == 0:
        N = N//2
        cnt += 1
    elif N % 2 == 1:
        N = N * 3 +1
        cnt += 1
        
        
print(cnt)
