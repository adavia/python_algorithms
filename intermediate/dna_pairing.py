def dna_pairing(st):
    res = []
    for item in st:
        if item == 'A':
            res.append([item, 'T'])
        elif item == 'T':
            res.append([item, 'A'])
        elif item == 'C':
            res.append([item, 'G'])
        elif item == 'G':
            res.append([item, 'C'])

    return res

print(dna_pairing('ATCGA'))
print(dna_pairing('TTGAG'))
print(dna_pairing('CTCTA'))
