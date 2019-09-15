def max_char_count(st):
    mapper = {}
    max_char = 0
    res = None

    for char in st:
        mapper[char] = mapper.get(char, 0) + 1

    for key, value in mapper.items():
        if value > max_char:
            res = key
            max_char = value

    return res

print(max_char_count('abbccccccd'))
print(max_char_count('apple 1231111'))
