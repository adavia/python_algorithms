def diff_array(a, b):
    # Esiest solution
    # set_a = set(a)
    # set_b = set(b)

    # return list(set_b ^ set_a)

    # Not very performant
    # res = []

    # for item in a:
    #     if item not in b:
    #         res.append(item)

    # for item in b:
    #     if item not in a:
    #         res.append(item)

    # return res

    arr = a + b
    res = []
    for item in arr:
        if item not in a or item not in b:
            res.append(item)

    return res


print(diff_array([1, 2, 3, 5], [1, 2, 3, 4, 5]))
print(diff_array([1, "calf", 3, "piglet"], [7, "filly"]))
print(diff_array([1, "calf", 3, "piglet"], [1, "calf", 3, 4]))
