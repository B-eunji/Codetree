while True:
    width, height, str = input().split()
    width = int(width)
    height = int(height)

    total = width*height

    print(total)

    if str == 'C':
        break
    