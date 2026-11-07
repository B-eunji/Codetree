arr = list(map(int, input().split()))

total = 0
for num in arr[::2]:
    total+= num

total_i = 0    
for num_i in arr[1:len(arr):2]:
    total_i += num_i

if total > total_i:
    print(total - total_i)
else:
    print(total_i - total)
