def factors(n):
    k = 1
    large_factors = []
    while k * k <= n:
        if n % k == 0:
            yield k
            if k != n // k:
                large_factors.append(n // k)
        k += 1
    for factor in large_factors[::-1]:
        yield factor

print(list(factors(100)))