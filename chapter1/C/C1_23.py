def array_index_handler(array, index, value):
    flage=False
    try:
        array[index] = value
    except IndexError:
        flage=True
    if flage:
        raise IndexError("Don't try buffer overflow attacks in Python!")

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    array_index_handler(array, 10, 7)  # This will raise an IndexError
    array_index_handler(array, 2, 7)   # This will succeed
    array_index_handler(array, -1, 27) # This will succeed
    array_index_handler(array, -12, 3) # This will raise an IndexError
