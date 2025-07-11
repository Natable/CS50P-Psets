def interpreter(x, y, z):
    floatX = float(x)
    floatZ = float(z)

    if y == '+':
        return round(floatX + floatZ, 1)
    elif y == '-':
        return round(floatX - floatZ, 1)
    elif y == '*':
        return round(floatX * floatZ, 1)
    elif y == '/':
        return round(floatX / floatZ, 1)
    else:
        print("You have no inputs")

def main():
    expression = input(("Expression: "))
    first, second, third = expression.split()
    result = interpreter(first, second, third)
    print(result)

main()
