def generate_strings(characters, current_string=""):
    # Base case: if all characters are used, yield the current string
    if not characters:
        yield current_string
        return

    # Recursive case: iterate through each character and create new strings
    for i in range(len(characters)):
        # Choose a character and exclude it from the remaining characters
        new_char = characters[i]
        remaining_chars = characters[:i] + characters[i+1:]

        # Yield strings from the recursive generator
        yield from generate_strings(remaining_chars, current_string + new_char)

# Using the generator
for permutation in generate_strings("catdog"):
    print(permutation)
