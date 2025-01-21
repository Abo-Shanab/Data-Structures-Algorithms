def sumsquares(k):
    return sum([x**2 for x in range(1,k) if x%2])

print(sumsquares(10))