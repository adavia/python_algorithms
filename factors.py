import math
def factors(n):
    # results = []
    # for k in range(1, n + 1):
    #     if n % k == 0:
    #         results.append(k)

    # return results

    # Using a list comprehension
    # factors = [k for k in range(1,n+1) if n % k == 0]

    # Using a generator
    
    # for k in range(1, n + 1):
    #     if n % k == 0: # divides evenly, thus k is a factor
    #         yield k # yield this factor as next result

    # Generator that computes factors
    k=1
    while k < math.sqrt(n): # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k

for n in factors(100):
    print(n)

