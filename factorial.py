def factorial(num):
    # Iterative approach
    # res = 1

    # while num > 1:
    #     res *= num
    #     num -= 1

    # return res

    # Recursive approach

    if num == 0:
        return 1
    else:
        return factorial(num - 1) * num

print(factorial(0))
print(factorial(5))
print(factorial(20))
