def mutation(arr):
    a = arr[0].lower()
    b = arr[1].lower()

    for char in b:
        if char not in a:
            return False

    return True

print(mutation(["hello", "hey"]))
print(mutation(["hello", "Hello"]))
