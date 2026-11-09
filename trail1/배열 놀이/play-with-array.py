N, Q = map(int, input().split())
nums = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))
    query_type = query[0]

    if query_type == 1:
        a = query[1]
        print(nums[a - 1])

    elif query_type == 2:
        b = query[1]
        answer = 0

        for i in range(N):
            if nums[i] == b:
                answer = i + 1
                break

        print(answer)

    else:
        s, e = query[1], query[2]
        print(*nums[s - 1:e])