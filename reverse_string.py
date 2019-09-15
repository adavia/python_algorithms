def reverse_string(s):
    # Simplified way to return a reversed string
    # return s[::-1]

    # Using join
    # st = ''.join(reversed(s))
    # return st

    # Using reverse
    # temp_list = list(s)
    # temp_list.reverse()
    # return ''.join(temp_list)

    # Another simplified version
    # res = ''

    # for char in s:
    #     res = char + res
    # return res

    # Using a while a loop
    res = ''
    i = len(s) - 1

    while i >= 0:
        res += s[i]
        i -= 1

    return res

print(reverse_string('hello'))
# print(reverse_string('Howdy'))
# print(reverse_string('Greetings from Earth'))
