def distinct(l):
    hash_ = {}
    for i in l:
        for x in l:
            if (x+i)%2:
                if str(i) not in hash_:
                    hash_[str(i)] = set()
                if str(x) not in hash_:
                    hash_[str(x)] = set()
                # Check if the pair has already been yielded
                if x not in hash_[str(i)] and i not in hash_[str(x)]:
                    yield (i, x)
                    hash_[str(i)].add(x)
                    hash_[str(x)].add(i)
    return
t=[]
tmp = [1,2,3,4,5,6,7,8,9,10]

for i in distinct(tmp):
    print(i)

