import time

def reverse(array):
    l=[]
    tmp=-1
    while True:
        try:
            l.append(array[tmp])
        except:
            return l
        tmp-=1
        

start_time = time.time()  # Record the start time
print(reverse([1,2,3,6,5,4,9,8,7,10]))
end_time = time.time()  # Record the end time

execution_time = end_time - start_time  # Calculate the elapsed time
print(f"Execution time: {execution_time} seconds")