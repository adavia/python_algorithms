def missing_letters(st):
    # Easiest
    # for i in range(len(st)):
    #     code = ord(st[i])
    #     if code != ord(st[0]) + i:
    #         return chr(ord(st[0]) + i)

    # return None

    for i in range(1, len(st)):
        if ord(st[i]) - ord(st[i - 1]) != 1:
            return chr(ord(st[i - 1]) + 1)
    return None

print(missing_letters('abce'))
print(missing_letters('abcdefghjklmno'))
print(missing_letters('stvwx'))
print(missing_letters('bcdf'))
print(missing_letters('abcdefghijklmnopqrstuvwxyz'))
