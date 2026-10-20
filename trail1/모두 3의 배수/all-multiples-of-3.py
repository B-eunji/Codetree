satis = False

for _ in range(5):
    i = int(input())
    if i % 3 == 0:
        satis = True
    else:
        satis = False
        break
if satis == True:
    print(1)
else:
    print(0)