# Using list comprehension to generate the desired list
result = [n * (n + 1) for n in range(10)]

# Printing the result to verify it
print(result)


# def patern(n,l=[],i=0,x=0):
#     if n == 0:
#         return l
#     l.append(x+(2*i))
#     return patern(n-1,l,i+1,x+(2*i))

# print(patern(10))
