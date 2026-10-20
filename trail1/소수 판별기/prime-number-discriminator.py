N = int(input())

satis = True

for i in range(2, N):
    if N % i == 0:
        satis = False

if satis == False:
    print("C")
else:
    print("P")