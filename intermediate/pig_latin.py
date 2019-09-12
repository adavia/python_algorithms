def pig_latin(st):
    lst = list(st)
    res = []

    if st[0] in 'aeiou':
        return st + 'way'

    while lst and lst[0] not in 'aeiou':
        consonant = lst.pop(0)
        res.append(consonant)

    return ''.join(lst + res) + 'ay'

print(pig_latin('glove'))
print(pig_latin('california'))
print(pig_latin('paragraphs'))
print(pig_latin('eight'))
print(pig_latin('zbbbk'))
