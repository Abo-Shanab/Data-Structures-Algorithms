def perform_arithmetic(n1, op, n2):
    if op == '+': return n1 + n2
    elif op == '-': return n1 - n2
    elif op == '/': return n1/n2
    elif op == '*': return n1*n2
    # else: return 'Invalid operand'

def convert_to_number(input_str):
    try:
        return float(input_str)
    except ValueError as e:
        print ('Invalid input')
        return None

def simple_calculator():
    operands = {'+', '-', '*', '/'}
    first_number = None
    second_number = None
    operand = None
    input_str = 'Start'
    while input_str != 'Exit' and input_str != '':
        input_str = input()
        if input_str == 'Exit' or input_str == '':
           break
        elif input_str == 'clr':
            first_number = second_number = operand = None
        elif first_number is None:
            first_number = convert_to_number(input_str)
        elif operand is None:
            if input_str in operands: operand = input_str
            else: first_number = convert_to_number(input_str)
        else: #Here we are expecting the second number
            second_number = convert_to_number(input_str)
            print (f'{first_number}{operand}{second_number} = {perform_arithmetic(first_number, operand, second_number)}')
            first_number = second_number = operand = None
    print('Exiting the calculator')
      
        
simple_calculator()