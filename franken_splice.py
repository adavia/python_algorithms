def franken_splice(a, b, num):
    b[num:num] = a
    return b

print(franken_splice([1, 2, 3], [4, 5, 6], 1))
print(franken_splice([1, 2], ["a", "b"], 1))
