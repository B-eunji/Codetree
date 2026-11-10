N_1, N_2 = map(int, input().split())

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

result = "No"

for i in range(N_1 - N_2 + 1):
    if list_1[i:i+N_2] == list_2:
        result = "Yes"
        break

print(result)