def chunky_monkey(arr, size):
    chunked = []

    for i in range(0, len(arr), size):
        chunked.append(arr[i:size + i])
    
    return chunked

print(chunky_monkey(["a", "b", "c", "d"], 2))
print(chunky_monkey([0, 1, 2, 3, 4, 5, 6], 3))
