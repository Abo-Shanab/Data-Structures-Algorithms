def minmax(data):
    min_ = data[0]
    max_ = data[0]
    for i in data:
        if i >max_:
            max_ = i
        if i < min_:
            min_ = i
    return (min_ , max_)
