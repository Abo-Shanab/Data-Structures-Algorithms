def reset():
    global current_value, pending_operation, operand
    current_value = 0
    pending_operation = None
    operand = None

def input_button(button):
    global current_value, pending_operation, operand
    try:
        if button.isdigit():
            operand = int(str((operand or "")) + button)
            return ""
        elif button in ['+', '-', '*', '/']:
            if pending_operation and operand is not None:
                calculate()
            else:
                current_value = operand if operand is not None else current_value
            pending_operation = button
            operand = None
            return ""
        elif button == '=':
            if pending_operation and operand is not None:
                calculate()
            pending_operation = None
            operand = None
            return display()
        elif button.lower() == 'c':
            reset()
            return ""
        else:
            return "Error: Invalid input\n"
    except ZeroDivisionError:
        reset()
        return "Error: Division by zero\n"

def calculate():
    global current_value, pending_operation, operand
    if pending_operation == '+':
        current_value += operand
    elif pending_operation == '-':
        current_value -= operand
    elif pending_operation == '*':
        current_value *= operand
    elif pending_operation == '/':
        current_value /= operand

def display():
    return f"Screen: {current_value}\n"

# Simulation of calculator buttons being pressed
def main():
    global current_value, pending_operation, operand
    reset()
    print("Welcome to the handheld calculator!")
    print("Enter digits, operators (+, -, *, /), '=', or 'C' to clear.")
    print("Type 'exit' to quit.")

    while True:
        button = input("Press a button: ").strip()
        if button.lower() == 'exit':
            print("Goodbye!")
            break
        output = input_button(button)
        print(output)

if __name__ == "__main__":
    main()
