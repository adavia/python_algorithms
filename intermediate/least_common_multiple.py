def least_common_multiple(lst):
    nums = list(range(min(lst), max(lst) + 1))

    # Find the greatest common divisor
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    lcm = nums[0] 

    for i in range(len(nums)):
        GCD = gcd(lcm, nums[i])
        lcm = (lcm * nums[i]) // GCD # least common multiple is a x b / gcd(a, b)

    return lcm

print(least_common_multiple([1, 3]))
print(least_common_multiple([5, 1]))
print(least_common_multiple([2, 10]))
print(least_common_multiple([1, 13]))
