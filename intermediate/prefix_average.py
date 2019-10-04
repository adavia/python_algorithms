def prefix_average(ls):
    """
    Return list such that, for all j, A[j] equals 
    average of S[0], ..., S[j].
    """

    length = len(ls)
    aux = [0] * length

    for i in range(length):
        total = 0
        for j in range(i + 1):
            print(j)
            total += ls[j]
        aux[i] = total / (i + 1)

    return aux


print(prefix_average([3, 5, 2, 9, 1]))
