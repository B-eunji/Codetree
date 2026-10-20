A, B = map(int,input().split())

result = False


for i in range(A, B+1):
    if 1920 % i == 0 and 2880 % i == 0:
        result = True

if result == True:
    print(1)
else:
    print(0)