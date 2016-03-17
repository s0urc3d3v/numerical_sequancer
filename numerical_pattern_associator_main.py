#usr/bin/python3
def main():
    print("Find mathmatical patterns by gathering arbitrary arithmatic data")
    x = input("test value")
    l = input("limit: ")
    operations = []
    control = True
    while (control):
        print(''"[operation] or "done"')
        print("0 = add, 1 = subtract, 2 = multiply, 3 = divide, 4 = mod, 5 = root, 6 = power")
        operation = input("operation: ")
        if lower(opeation) is 'done':
            control = False
        else:
            operations.append(operation)

    outputs = []
    for i in range(0, len(operations)):
        if operations[i] is 0:
            outputs.append(add(x, l))
        elif operations[i] is 1:
            outputs.append(subtract(x, l))
        elif operations[i] is 2:
            outputs.append(multiply(x, l))
        elif operations[i] is 3:
            outputs.append(divide(x, l))
        elif operations[i] is 4:
            outputs.append(mod(x, l))
        elif operations[i] is 5:
            r = input("Please enter root: ")
            outputs.append(root(x, r, l))
        elif operations[i] is 6:
            m = input("Please enter power: ")
            outputs.append(power(x, m, l))
        else:
            print("UNSUPPORTED OPERATION")

    output_data(outputs)

def add(x, limit):
    out = []
    for i in range(0, limit):
        out.append(x + i)
    return out
def subtract(x, limit):
    out = []
    for i in range(0, limit):
        out.append(x - i)
    return out
def multiply(x, limit):
    out = []
    for i in range(0, limit):
        out.append(x * i)
    return out
def divide(x, limit):
    out = []
    for i in range(0, limit):
        out.append(x / i)
    return out

def mod(x, limit):
    out = []
    for i in range(0, limit):
        out.append(x % i)
    return out

def root(x, root, limit):
    out = []
    root = 1 / root
    for i in range(0, limit):
        out.append(root**x)
    return out
def power(x, power, limit):
    out = []
    y = x
    for i in range(0, limit):
        for z in range(0, power):
            y = y * x
        out.append(y)
    return out

def output_data(data):
    for i in range(0, len(data)):
        for k in range(0, len(data[i]))
            print((data[i])[k])
        print("\n")

main()
