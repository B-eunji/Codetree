arr = ['L','E','B','R','O','S']

word = input()

idx = -1

for i in range(len(arr)):
    if word == arr[i]:
        idx = i
        break

if idx != -1:
    print(idx)
else:
    print("None")