def sumsquares(k):
    for i in range(0,k):
        if i%2:
            yield i**2
sum_ = 0
for i in sumsquares(10):
    sum_ += i  
print(sum_)
