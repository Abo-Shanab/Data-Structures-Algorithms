from time import time
import math

# Function to repeatedly divide a number by 2 until it is less than or equal to 2
def repeatedly_divide(i):
    count = 0
    while i > 2:
        i /= 2
        count += 1
    return count

# Measure the time taken by repeatedly_divide function
start_time = time()
print(repeatedly_divide(100))
end_time = time()
print(f"Time taken by repeatedly_divide: {end_time - start_time} seconds")

# Function to find the floor value of log base 2 of a number
def find_log2(number):
    assert number > 2, 'The number should be greater than 2'
    return int(math.log(number, 2) // 1)

# Measure the time taken by find_log2 function
start_time = time()
print(find_log2(100))
end_time = time()
print(f"Time taken by find_log2: {end_time - start_time} seconds")