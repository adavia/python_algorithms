from math import sqrt

def sum_primes(num):
    # Easiest solution
    # total = 0

    # def is_prime(num):
    #     for n in range(2, num):
    #         if num % n == 0:
    #             return False
    #     return True

    # for n in range(num + 1):
    #     if n > 1:
    #         if is_prime(n):
    #             total += n

    # return total

    total = 0

    def only_primes(n):
        prev = n - 1
        while prev > 1 and prev >= sqrt(n):
            if (n % prev) == 0:
                return False
            prev -= 1
        return True

    for n in range(2, num + 1):
        if only_primes(n):
            total += n

    return total

print(sum_primes(10))
print(sum_primes(977))
