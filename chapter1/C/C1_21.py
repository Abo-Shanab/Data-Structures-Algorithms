def reverse_input():
    lines=[]
    while True:
        try:
            line = input()
            if line=="": raise EOFError 
            lines.append(line)
        except EOFError:
            break
    print(lines[::-1])

reverse_input()