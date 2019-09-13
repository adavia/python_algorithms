def sum_odd_fib(num):
    # Not really good
    # prev = 0
    # curr = 1
    # total = 0

    # while curr <= num:
    #     if curr % 2 != 0:
    #         total += curr
    #     curr = prev + curr
    #     prev = curr - prev

    # return total

    # Better
    total = 0

    def get_fib_nums(num):
        prev = 0
        curr = 1

        while curr <= num:
            yield curr
            prev, curr = curr, curr + prev

    for item in get_fib_nums(num):
        if item % 2 != 0:
            total += item

    return total

print(sum_odd_fib(4))
print(sum_odd_fib(1))
print(sum_odd_fib(75024))
print(sum_odd_fib(75025))
print(sum_odd_fib(1000))
