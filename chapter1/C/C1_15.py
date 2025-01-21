def distinct(l):
    for i in l:
        for x in l:
            if x == l :
                return False
    return True

print(distinct([1,2,3,4,5,6,7,8,9,10]))