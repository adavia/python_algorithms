def find_index(arr, num):
    arr.append(num)
    arr.sort()
    return arr.index(num)

print(find_index([3, 10, 5], 3))
print(find_index([5, 3, 20, 3], 5))
