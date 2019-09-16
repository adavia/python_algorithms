def is_anagram(str_a, str_b):
    # Solution 1
    # if len(str_a) != len(str_b):
    #     return False

    # result = list(str_b)
    # i = 0

    # while i < len(str_a):
    #     if str_a[i] in result:
    #         result.remove(str_a[i])
    #     i += 1

    # return not result

    # Solution 2
    # if len(str_a) != len(str_b):
    #     return False

    # lst = list(str_b)
    # i = 0

    # while i < len(str_a):
    #     j = 0 
    #     found = False
    #     while j < len(str_b) and not found:
    #         if str_a[i] == lst[j]:
    #             found = True
    #         else:
    #             j += 1

    #     if found:
    #         lst[j] = None
    #     else:
    #         return False
    #     i += 1

    # return True

    # Solution 3

    if len(str_a) != len(str_b):
        return False

    mapp_chars_a = {}
    mapp_chars_b = {}

    for char in str_a:
        mapp_chars_a[char] = mapp_chars_a.get(char, 0) + 1

    for char in str_b:
        mapp_chars_b[char] = mapp_chars_b.get(char, 0) + 1

    for item in str_a:
        if item not in mapp_chars_b or mapp_chars_a[item] != mapp_chars_b[item]:
            return False

    return True

print(is_anagram('rail safety', 'fairy tales'))
print(is_anagram('Hi there', 'Bye there'))
print(is_anagram('mycar', 'racym'))
print(is_anagram('abcd', 'dbcb'))
