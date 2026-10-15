N = int(input())

cnt = 0

for num in range(1, N+1):
    cnt += 1
    if N//num <= 1:
        break
    
    N = N // num

print(cnt)