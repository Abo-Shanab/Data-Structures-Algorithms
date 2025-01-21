def sumsquares(k):
    for i in range(1,k):
        yield i**2
sum_ = 0
for i in sumsquares(10):
    sum_ += i  
print(sum_)
