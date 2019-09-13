def drop_elements(lst, func):
    found = None
    for i in range(len(lst)):
        if func(lst[i]):
            found = i
            break

    if found is not None:
        return lst[found:]
    
    return []

print(drop_elements([1, 2, 3], lambda n: n > 0))
print(drop_elements([1, 2, 3, 4], lambda n: n >= 3))
print(drop_elements([0, 1, 0, 1], lambda n: n == 1))
print(drop_elements([1, 2, 3, 7, 4], lambda n: n > 3))
print(drop_elements([1, 2, 3, 9, 2], lambda n: n > 2))
print(drop_elements([1, 2, 3, 4], lambda n: n > 5))
