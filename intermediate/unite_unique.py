def unite_unique(*args):
    values = []
    result = []

    for lst in args:
        values += lst

    for item in values:
        if item not in result:
            result.append(item)

    return result
        
print(unite_unique([1, 3, 2], [5, 2, 1, 4], [2, 1]))
print(unite_unique([1, 3, 2], [1, [5]], [2, [4]]))
print(unite_unique([1, 2, 3], [5, 2, 1]))
print(unite_unique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]))

