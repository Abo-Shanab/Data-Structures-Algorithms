def remove_punctuation(data, punc = {'.', ',', '!', '?', ':', ';'}):
    new_array = []
    for char in data:
        if not char in punc: new_array.append(char)
    return ''.join(new_array)
