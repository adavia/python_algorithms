def reverse_string(s):
    # Simplified way to return a reversed string
    # return s[::-1]

    # Using a while a loop
    res = ''
    i = len(s) - 1

    while i >= 0:
        res += s[i]
        i -= 1

    return res

print(reverse_string('hello'))
print(reverse_string('Howdy'))
print(reverse_string('Greetings from Earth'))
