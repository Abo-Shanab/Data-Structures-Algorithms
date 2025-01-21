def claculater():
    print('This is a calculator.')
    values={"first number":None,"second number":None,"operator":None}
    operators=["+","-","*","/"]
    flage=""
    while True:
        try:
            if values["first number"]==None:
                flage="first number"
                values["first number"] = float(input('Please input the first number:'))
            if values["second number"]==None:
                flage="second number"
                values["second number"] = float(input('Please input the second number:'))
            if values["operator"]==None:
                flage="operator"
                tmp = input('Please input the operator:')
                if tmp in operators: values["operator"]=tmp
                else: raise Exception
        except:
            print(f'Invalid input for {flage}')
            continue
        print(f"{values['first number']} {values['operator']} {values['second number']} = {claculate(values)}")
        values={"first number":None,"second number":None,"operator":None}

def claculate(values):
    if values["operator"] == '+': return values["first number"] + values["second number"]
    elif values["operator"] == '-': return values["first number"] - values["second number"]
    elif values["operator"] == '/': return values["first number"]/values["second number"]
    elif values["operator"] == '*': return values["first number"]*values["second number"]

claculater()