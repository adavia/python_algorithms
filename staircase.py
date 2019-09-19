def staircase(num):
    # Easiest solution
    # for i in range(num + 1):
    #     print(' ' * (num - i) + '#' * i)

    for row in range(0, num):
        stair = ''
        for column in range(0, num):
            if column <= row:
                stair += '#'
            else:
                stair += ' '

        print(stair)

staircase(3)
