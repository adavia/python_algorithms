def staircase(num):
    # Print a staircase
    for i in range(num + 1):
        print(' ' * (num - i) + '#' * i)

print(staircase(7))
