def pyramid(num):
    mid = (2 * num - 1) // 2

    for row in range(0, num):
        level = ''
        for column in range(0, num * 2 - 1):
            if mid - row <= column and mid + row >= column:
                level += '#'
            else:
                level += ' '

        print(level)

pyramid(8)
