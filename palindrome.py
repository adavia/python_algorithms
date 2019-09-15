def is_palindrome(st):
    mid = len(st) // 2
    i = 0

    while i < mid:
        if st[i] != st[(len(st) - 1) - i]:
            return False
        i += 1

    return True

print(is_palindrome('redivider'))
print(is_palindrome('racecar'))
print(is_palindrome('johnny'))
print(is_palindrome('deified'))
print(is_palindrome('madam'))
