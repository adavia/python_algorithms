def find_element(arr, func):
    for item in arr:
        if func(item):
            return item

    return None

print(find_element([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0))
print(find_element([1, 3, 5, 9], lambda num: num % 2 == 0))
