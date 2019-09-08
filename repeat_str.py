def repeat_str(st, num):
    # Easiest solution
    # return st * num

    res = ''

    for i in range(num):
        res += st

    return res

print(repeat_str('*', 3))
print(repeat_str('abc', 3))
print(repeat_str('abc', -2))
