def sum_all(arr):
    res = 0
    for i in range(arr[0], arr[1] + 1):
        res += i

    return res

print(sum_all([1, 4]))
print(sum_all([5, 10]))
