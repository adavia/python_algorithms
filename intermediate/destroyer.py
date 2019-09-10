def destroyer(arr, *args):
    # Esiest solution
    # filtered = filter(lambda num: num not in args, arr)
    # return list(filtered)

    mapper = {}

    for item in args:
        mapper[item] = True
        #mapper[num] = mapper.get(num, 0) + 1

    return [item for item in arr if item not in mapper]

print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))
print(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3))
print(destroyer(["tree", "hamburger", 53], "tree", 53))
