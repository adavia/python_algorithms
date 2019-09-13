def list_flatten(lst):
    result = []

    for item in lst:
        if type(item) is list:
            result += list_flatten(item)
        else:
            result.append(item)

    return result

print(list_flatten([1, [2], [3, [[4]]]]))
print(list_flatten([[["a"]], [["b"]]]))
print(list_flatten([1, {}, [3, [[4]]]]))
