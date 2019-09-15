def reverse_int(num):
    # Easiest solution
    to_s = str(abs(num))
    if num < 0:
        return int(to_s[::-1]) * -1

    return int(to_s[::-1])

print(reverse_int(982734))
print(reverse_int(500))
print(reverse_int(-15))
print(reverse_int(-90))
