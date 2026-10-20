a, b, c = map(int, input().split())
satis = False
for num in range(a, b+1):
    if num % c == 0:
        satis = True

if satis == False:
    print("NO")
else:
    print("YES")