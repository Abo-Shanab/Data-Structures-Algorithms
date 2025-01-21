from random import randrange

def choice(data):
    length = len(data)
    if length==0:
        raise "error"
    return data[randrange(0,length)]

print(choice([1,2,3,4,5,6,7,8,9]))