def dot_product(a,b):
    length = len(a)
    c=[]
    for i in range(length):
        c.append(a[i]*b[i])
    return c

print(dot_product([1,2,3],[4,5,6]))