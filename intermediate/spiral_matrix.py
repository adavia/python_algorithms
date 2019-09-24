def spiral(num):

    """ Build a matrix spiral """

    # [   SC0               EC4
    #   SR0[1,  2,  3,  4,  5]
    #      [16, 17, 18, 19, 6]
    #      [15, 24, 25, 20, 7]
    #      [14, 23, 22, 21, 8]
    #   ER4[13, 12, 11, 10, 9]
    # ]

    results = [[None for n in range(0 , num)] for n in range(0, num)]
    counter = 1
    start_row = 0
    end_row = num - 1
    start_column = 0
    end_column = num - 1

    while start_column <= end_column and start_row <= end_row:
        for i in range(start_column, end_column + 1):
            results[start_row][i] = counter
            counter += 1
        start_row += 1

        for i in range(start_row, end_row + 1):
            results[i][end_column] = counter
            counter += 1

        end_column -= 1

        for i in range(end_column, start_column - 1, -1):
            results[end_row][i] = counter
            counter += 1

        end_row -= 1

        for i in range(end_row, start_row - 1, -1):
            results[i][start_column] = counter
            counter += 1

        start_column += 1

    return results

print(spiral(5))
